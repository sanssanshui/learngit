这个是由本人 George 书写创建的 前后端分离项目

做的是一个 学生登录功能 +  
对学生数据库(student_management) 中的 studentinfo 表的信息进行 CRUD 的可视化操作

使用 Vite + vue3 （前端） SpringBoot(后端) 编写

##项目体验指引##

1.进入 SpringBoot 文件夹
student_fronted 前端 vue
student_management 后端 java 语言 + SpringBoot 框架

2.前端运行的话，需要 cd 到 student_fronted 文件夹中 再执行 npm run dev 命令 可正常启动
比如 当前在 SpringBoot 文件夹  
 cd ./student_fronted
npm run dev
即可

3.要确保后端正常运行，请注意下面这个资源文件的内容配置
student_management\src\main\resources\application.properties

// 以下是我的连接配置

使用的是 Mysql 5.7 版本 创建了一个 student_management 这样一个数据库

// 这个位置是你创建自定义的数据库名字，可以相同也可以自定义

spring.datasource.url=jdbc:mysql://localhost:3306/**student_management**?characterEncoding=UTF-8

// 这里默认是 root 用户

spring.datasource.username=root

//密码这边就是你当初连接 Mysql 的那个密码

spring.datasource.password=123456  
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true

// 这里需要注意一下了，我使用的是 MYSQL 5.7 版本，根据实际情况做相应的调整即可，具体可以百度一下

spring.jpa.properties.hibernate.dialect=org.hibernate.community.dialect.MySQL57Dialect

// 我指定的后端应用端口

server.port=8081
