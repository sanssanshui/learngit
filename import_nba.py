import pymysql

# -------------------------- 1. 配置数据库连接信息（需修改为你的实际信息）--------------------------
DB_CONFIG = {
    "host": "localhost",    # 本地数据库
    "user": "root",         # 你的 MySQL 用户名
    "password": "root",   # 你的 MySQL 密码（替换成真实密码）
    "db": "nba_player",      # 数据库名（已创建的 nba_stats）
    "charset": "utf8mb4",   # 编码一致，避免中文乱码
    "port": 3306            # 默认端口
}

# -------------------------- 2. 连接数据库并导入数据 --------------------------
def import_nba_data():
    # 1. 建立数据库连接
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()  # 创建游标（用于执行 SQL）
        print("数据库连接成功！")
    except Exception as e:
        print(f"数据库连接失败！错误：{e}")
        return

    # 2. 读取 nba.txt 并解析数据（跳过第一行表头）
    try:
        with open("nba.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()  # 读取所有行
            for idx, line in enumerate(lines):
                # 跳过第一行表头（索引为 0 的行）
                if idx == 0:
                    print("跳过表头行：", line.strip())
                    continue

                # 清理行数据（去除前后空格、换行符）
                line = line.strip()
                if not line:  # 跳过空行（若文件有空白行）
                    continue

                # -------------------------- 关键：解析每行数据 --------------------------
                # 示例行格式："排名: 1  姓名:扬尼斯-阿德托昆博  球队:雄鹿  得分:40.00"
                # 按 "  "（两个空格）分割数据（根据你的 nba.txt 格式调整，不可用单个空格）
                data_parts = line.split("  ")
                if len(data_parts) != 4:  # 若分割后不是4部分，视为无效数据，跳过
                    print(f"跳过无效数据行：{line}（格式错误）")
                    continue

                # 提取各字段值（去除前缀，如 "排名: "）
                ranking_str = data_parts[0].replace("排名: ", "")  # 提取 "1"
                name = data_parts[1].replace("姓名:", "")          # 提取 "扬尼斯-阿德托昆博"
                team = data_parts[2].replace("球队:", "")          # 提取 "雄鹿"
                score_str = data_parts[3].replace("得分:", "")      # 提取 "40.00"

                # 数据类型转换（排名→整数，得分→小数，避免插入数据库报错）
                try:
                    ranking = int(ranking_str)
                    score = float(score_str)
                except ValueError:
                    print(f"跳过无效数据行：{line}（排名/得分不是数字）")
                    continue

                # -------------------------- 3. 插入数据到数据库 --------------------------
                # SQL 插入语句（用 %s 占位符，避免 SQL 注入）
                insert_sql = """
                    INSERT INTO players (ranking, name, team, score)
                    VALUES (%s, %s, %s, %s)
                """
                # 执行插入（参数顺序与 SQL 占位符对应）
                cursor.execute(insert_sql, (ranking, name, team, score))
                print(f"成功插入：排名{ranking} | {name} | {team} | {score}分")

        # 提交事务（批量插入后必须提交，否则数据不生效）
        conn.commit()
        print(f"\n数据导入完成！共导入 {idx} 条有效球员数据（已跳过表头）")

    except Exception as e:
        # 若出错，回滚事务（避免部分数据插入）
        conn.rollback()
        print(f"数据导入失败！错误：{e}")
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()
        print("数据库连接已关闭")

# 执行导入函数
if __name__ == "__main__":
    import_nba_data()