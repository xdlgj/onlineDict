项目开发流程

需求分析-->概要设置-->项目计划-->详细设计-->编码测试-->项目测试-->调试修改-->项目发布

需求分析：理解用户需求，提供需求文档，和用户进行确认
	1、功能：部署环境，对应人群，并发量，流量控制，特殊需求，可行性分析
概要设计：对项目进行初步的分析和整体设计，形成概要设计文档
	1、确定项目技术思路，确定使用框架等，分为多少模块
项目计划：指定项目的前去后继开发流程，给定项目周期，设置时间节点，做好项目分工，作为项目负责人最重要的工作之一
	1、project 甘特图
详细设计：项目具体实现技术，项目的技术阐述。编码阐述，逻辑流程，数据结构，每个模块功能等等
	1、visio   mindmanage
编码测试：按照预定设计编码实现。进行bug调试，进行技术公关，进行基本的代码测试，注释占15%--20%
	1、pycharm  sublime vim  atom
项目测试：对项目的功能进行集中测，整理测试文档，对项目结果负责，测试说明书
调试修改：根据测试即结果进行修改
项目发布：完成项目的上线部署和发布工作，编写使用说明或者操作说明
	github 
项目注意事项
	能够按时完成项目和项目时间不足
	小组中人员能力差距越大越容易发生冲突
	没有按照计划完成任务
电子辞典
客户端：
	1、用户注册
	2、登录，登录之后才能进行其他操作
	3、单词查询
	4、查看历史记录
	5、退出
服务器端
	1、使用数据库存储注册人员信息和历史记录
	2、要允许多个用户能够同时登录
	3、建议使用tcp完成网络传输
	4、单词使用单词本进行处理
	提示：
		1、单词本每个单词占一行
		2、单词和解释之间一定要有空格
		3、单词按照顺序排列
客户端框架（多少模块，两层界面怎么切换）
服务器端框架（使用什么方式并发，多少个功能模块）
使用什么方式通信
数据表设计（几个表，每个表存存什么）
********************************************************************************
1、使用socketserver搭建多线tcp程服务器,
	1.创建服务器类
	2.创建处理类
	3.使用创建的服务器类来创建服务器对象
	4.运行服务器
2、实现第一个界面（登录，注册，退出）
3、实现退出功能
4、实现登录功能，如果密码不正确可以一直输入（会出现粘包现象），直到正确为止，
	如果用户不存在，将其跳转到主界面
5、实现注册功能，注册成功跳转主界面进行登录
6、实现查询功能  	









