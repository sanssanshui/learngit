CREATE TABLE players(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    ranking INT COMMENT '排名',
    name VARCHAR(255) COMMENT '球员姓名',
    team VARCHAR(255) COMMENT '球队名称',
    score DECIMAL(5,2) COMMENT '得分'
) COMMENT '';