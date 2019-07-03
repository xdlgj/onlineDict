from socketserver import *
import sys
from mysqlPy import MysqlPy
import time

def do_login(connfd):
	'''登录操作'''
	connfd.send('请输入用户名：'.encode())
	username = connfd.recv(1024).decode()
	#print(username)
	#去数据库中查找，如果存在提示提供输入密码，如果不存在提示用户注册
	sql = 'select * from user where name = "%s";' % username
	#print(sql)
	mp = MysqlPy('localhost','debian-sys-maint','Lo0r79JmxvMFNtA2','onlineDict',3306)      												 
	res = mp.myFetchone(sql)
	# print(res)# 一个元素为每个字段的元组
	if not res:
		#用户不存在，将跳转到主界面
		connfd.send('用户名不存在'.encode())
		time.sleep(0.1)
		login_screen(connfd)
	else:
		num = 0 # 记录输入密码的次数
		while True:
			connfd.send('请输入密码：'.encode())
			pwd = connfd.recv(1024).decode()
			#print(pwd)
			if pwd == res[2]:
				#登录成功开始使用词典
				dic_screen(connfd)
				break
			else:
				num += 1
				if num == 3:
					connfd.send('请30秒后重试'.encode())
					num = 0
					time.sleep(30)
				else:
					connfd.send('fail'.encode())
					time.sleep(0.1)#防止粘包

def do_register(connfd):
	'''注册操作'''
	while True:
		connfd.send('请输入新用户名：'.encode())
		username = connfd.recv(1024).decode()
		connfd.send('请输入新密码：'.encode())
		pwd = connfd.recv(1024).decode()
		sql = "insert into user values(0,'%s','%s')"%(username,pwd)
		mp = MysqlPy('localhost','debian-sys-maint','Lo0r79JmxvMFNtA2','onlineDict',3306)
		res = mp.myexecute(sql)
		#print(res)
		if not res:
			#注册失败
			connfd.send('fail'.encode())
			time.sleep(0.1)
			login_screen(connfd)
		else:
			#注册成功
			connfd.send('注册成功'.encode())
			time.sleep(0.1)
			login_screen(connfd)#注册成功跳转到主界面
			break


def do_quit(connfd):
	'''退出操作'''
	connfd.send('欢迎下次光临'.encode())
	connfd.close()

def  login_screen(connfd):
	'''展示登录主界面'''
	connfd.send('L：登录\nR：注册\nQ：退出'.encode())
	while True:
		data = connfd.recv(1024).decode()
		if data == 'L':
			do_login(connfd)
		elif data == 'R':
			do_register(connfd)
		elif data == 'Q':
			do_quit(connfd)

def do_lookup(connfd):
	'''查找单词'''
	try:
		with open('dict.txt','rb') as f:
			connfd.send('请输入你要查找的单词：'.encode())
			word = connfd.recv(1024).decode()
			while True:
				data = f.readline().decode('gbk')
				l = data.split()
				if not l:
					connfd.send('没有找到你想要的结果'.encode())
					break
				elif l[0] == word:
					res = ' '.join(l[1:])
					connfd.send(("意思是："+res).encode())
					break
	except OSError:
		print('文件打开失败')
		return

def do_history(connfd):
	'''显示历史记录'''

	#需要的得到当前的用户名
	username = connfd.recv(1024).decode()
	sql = "select word,date from history where name = '%s' order by date DESC"%username
	mp = MysqlPy('localhost','debian-sys-maint','Lo0r79JmxvMFNtA2','onlineDict',3306)
	res = str(mp.myFetchmany(sql,10))#得到的元组转为字符串
	connfd.send(res.encode())

def dic_screen(connfd):
	'''展示字典操作界面'''
	connfd.send('F：查找\nH：历史记录\nE：退出'.encode())
	while True:
		data = connfd.recv(1024).decode()
		if data == 'F':
			do_lookup(connfd)
		elif data == 'H':
			do_history(connfd)
		elif data == 'E':
			login_screen(connfd)#退出到登录主界面

def main():
	# 1.创建多进程TCP服务器类
	class Server(ThreadingTCPServer):
		pass

	# 2.创建流式套接字处理类
	class Handler(StreamRequestHandler):
		# 当客户端连接进来时候会自动调用该函数处理客户端请求时间
		def handle(self):
			addr = self.client_address
			print("connected from ", addr) # ('127.0.0.1', 52578)
			# self.requset为tcp中为我们自动生成的和客户端交互的套接字
			login_screen(self.request)

	if len(sys.argv) != 3:
		print('argv error')
		return
	ADDR  = (sys.argv[1],int(sys.argv[2]))
	# 3.创建服务器对象
	server = Server(ADDR,Handler)
	# 4.运行服务器
	server.serve_forever()

if __name__ == '__main__':
	main()