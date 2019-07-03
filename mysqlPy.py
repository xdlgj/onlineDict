from pymysql import *

class MysqlPy:
	def __init__(self,h,u,p,db,port,charset='utf8'):
		self.host = h
		self.user =  u
		self.pwd =  p
		self.database = db
		self.port = port
		self.charset = charset

	def open(self):
		'''连接数据库'''
		#print('准备连接数据库')
		self.conn = connect(self.host, self.user, self.pwd, self.database, self.port, charset=self.charset)
		#创建游标
		self.cur = self.conn.cursor()

	def close(self):
		'''关闭游标，断开与数据库的连接'''
		self.cur.close()
		self.cur.close()

	def myexecute(self,sql):
		'''执行SQL语句'''
		self.open()
		#print("数据库已连接")
		try:
			self.cur.execute(sql)
			self.conn.commit()
			return 'success'
		except Exception as e:
			self.conn.rollback()
			return 
		finally:
			self.close() 

	def myFetchone(self,sql):
		'''得到一条记录'''
		try:
			self.open()
			#print('已经连接到数据库')
			self.cur.execute(sql)
			data = self.cur.fetchone()
			return data
		except Exception as e:
			return 
		finally:
			self.close()

	def myFetchmany(self,sql,n):
		'''得到多条记录条记录'''
		try:
			self.open()
			#print('已经连接到数据库')
			self.cur.execute(sql)
			data = self.cur.fetchmany(n)
			return data
		except Exception as e:
			return 
		finally:
			self.close()

