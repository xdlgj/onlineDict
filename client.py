from socket import *
import sys
from mysqlPy import MysqlPy
import time
import re

def do_login(sockfd):
	'''实现登录功能'''
	global L #保存当前的用户名
	info = sockfd.recv(1024).decode()
	username = input(info) or '0'#输入用户名,如果不输入默认为0
	sockfd.send(username.encode())
	while True:
		data = sockfd.recv(1024).decode()
		if data == '用户名不存在':
			print(data)
			login_screen(sockfd)
			break
		pwd = input(data) or '0'#输入密码,防止输入空
		sockfd.send(pwd.encode())
		res = sockfd.recv(2014).decode()
		if res == 'fail':
			pass
		elif res == "请30秒后重试":
			print(res)
		else:
			L.append(username)
			dic_screen(sockfd,res)
			break
			

def do_register(sockfd):
	while True:
		info = sockfd.recv(1024).decode()
		username = input(info) or '0'#输入用户名
		sockfd.send(username.encode())
		info = sockfd.recv(1024).decode()
		pwd = input(info) or '0'#输入密码
		sockfd.send(pwd.encode())
		#注册结果
		res = sockfd.recv(1024).decode()
		if res == 'fail':
			print('此用户已存在，注册失败！')
			login_screen(sockfd)
		else:
			#注册成功
			print(res)
			login_screen(sockfd)
			break

def do_quit(sockfd):
	'''退出操作'''
	data = sockfd.recv(1024)
	print(data.decode())
	sockfd.close()
	exit()

def login_screen(sockfd):
	'''登录主界面'''
	info = sockfd.recv(1024).decode()
	print(info)#打印界面
	while True:
		data = input('发送：')
		sockfd.send(data.encode())
		if data == 'L':
			do_login(sockfd)
		elif data == 'R':
			do_register(sockfd)
		elif data == 'Q':
			do_quit(sockfd)
			return
		else:
			print('输入不合法！！')
			continue
		
		# data = sockfd.recv(1024)
		# print(data.decode())


def do_lookup(sockfd):
	'''查找单词'''
	username = L[0]
	data = sockfd.recv(1024).decode()
	word = input(data)
	#每次查找将查找的单词存在数据库，以便查看历史记录
	sql = "insert into history(name,word) values('%s','%s')"%(username,word)
	#print(sql)
	mp = MysqlPy('localhost','debian-sys-maint','Lo0r79JmxvMFNtA2','onlineDict',3306)
	mp.myexecute(sql)

	sockfd.send(word.encode())
	res = sockfd.recv(1024).decode()
	print(res)

def do_history(sockfd):
	username = L[0]
	#print(username)
	time.sleep(0.1)
	sockfd.send(username.encode())
	res = sockfd.recv(1024).decode()

	l = re.findall(r"\(\'.*?\)\)",res)#?将贪婪模式变为非贪婪模式

	for i in l:
		print(i)

def dic_screen(sockfd,res):
	'''字典操作界面'''
	print('欢迎使用林婧词典\n',res,sep = '')
	while True:
		data = input('操作命令：')
		sockfd.send(data.encode())
		if data == 'F':
			do_lookup(sockfd)
		elif data == 'H':
			do_history(sockfd)
		elif data == 'E':
			global L
			#print(L)
			L.pop()
			#print(L)
			login_screen(sockfd)#t退出到登录主界面
			return
		else:
			print('输入不合法！！')
			continue

def main():
	if len(sys.argv) != 3:
		print("argv error")
		return
	HOST = sys.argv[1]
	PORT = int(sys.argv[2])
	ADDR = (HOST,PORT)
	# 创建流式套接字
	sockfd = socket(AF_INET,SOCK_STREAM)
	# 连接服务器
	sockfd.connect(ADDR)
	login_screen(sockfd)
	
L = []#用来保存当前的用户名

if __name__ == '__main__':
	main()