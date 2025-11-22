const express = require('express');
const fs = require('fs');
const cors = require('cors');
const path = require('path');

const app = express();
app.use(cors()); // 允许所有来源的前端页面访问

const PORT = 3001; // 使用一个端口号，比如 3001

// 定义一个 API 接口，用于提供动态数据
app.get('/api/quote', (req, res) => {
  // 读取我们的 JSON 文件
  fs.readFile('quotes.json', 'utf8', (err, data) => {
    if (err) {
      // 如果读取文件出错，返回服务器错误
      return res.status(500).send('Error reading quotes data.');
    }
    
    const quotesData = JSON.parse(data);
    const quotes = quotesData.quotes;
    
    // 从名言数组中随机选取一个
    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    
    // 将这句随机名言作为 JSON 数据返回给前端
    res.json({ quote: randomQuote });
  });
});

app.get('/', (req, res)=>{
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`后端数据服务器正在运行在 http://localhost:${PORT}`);
  console.log(`你可以通过访问 http://localhost:${PORT}/api/quote 来获取动态数据`);
});