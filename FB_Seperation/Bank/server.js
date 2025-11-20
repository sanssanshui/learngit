const express = require('express');
const fs = require('fs');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = 3001;
const DB_FILE = path.join(__dirname, 'db.json');

// 中间件 (Middleware)
app.use(cors());
app.use(express.json()); // 非常重要！让 Express 能够解析 POST 请求中的 JSON 数据

// --- API 路由 ---

// GET /api/account - 获取完整的账户信息
app.get('/api/account', (req, res) => {
  fs.readFile(DB_FILE, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ error: '无法读取账户数据' });
    }
    res.json(JSON.parse(data).account);
  });
});

// POST /api/transaction - 处理一笔新交易 (存款或取款)
app.post('/api/transaction', (req, res) => {
  const { type, amount } = req.body;
  const transactionAmount = parseFloat(amount);

  if (!type || !transactionAmount || transactionAmount <= 0) {
    return res.status(400).json({ error: '无效的交易类型或金额' });
  }

  fs.readFile(DB_FILE, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ error: '无法读取账户数据' });
    }

    const db = JSON.parse(data);
    let currentBalance = db.account.balance;

    if (type === 'withdraw' && currentBalance < transactionAmount) {
      return res.status(400).json({ error: '余额不足' });
    }

    // 更新余额
    currentBalance = (type === 'deposit') 
      ? currentBalance + transactionAmount 
      : currentBalance - transactionAmount;
    
    db.account.balance = parseFloat(currentBalance.toFixed(2));

    // 创建新交易记录
    const newTransaction = {
      id: Date.now(), // 使用时间戳作为唯一ID
      type: type,
      amount: transactionAmount,
      timestamp: new Date().toISOString()
    };
    db.account.transactions.unshift(newTransaction); // unshift 加到数组最前面

    // 将更新写回文件
    fs.writeFile(DB_FILE, JSON.stringify(db, null, 2), (err) => {
      if (err) {
        return res.status(500).json({ error: '无法保存账户数据' });
      }
      // 返回更新后的整个账户信息
      res.json(db.account);
    });
  });
});

// --- 根路由：提供前端页面 ---
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// 为了让CSS文件也能被正确加载，我们需要一个静态文件服务
app.use(express.static(__dirname)); 

app.listen(PORT, () => {
  console.log(`SimuBank 服务器已在 http://localhost:${PORT} 启动`);
});