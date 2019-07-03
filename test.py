

# def f():
# 	try:
# 		print('try')
# 		return
# 	except:
# 		return
# 	finally:
# 		print('OK')

# sql = "insert into user values(0,'%s','%s')"%('xx','bb')

# print(sql)

# print(None == 's')

# try:
# 	with open('dict.txt','r') as f:
# 		while True:
# 			data = f.readline()
		
# 			l = data.split()
	


# 			if l[0] == 'abbey':
# 				print(' '.join(l[1:]))
# 				break
# except OSError:
# 	print('文件打开失败')
	
# try:
# 	with open('dict.txt','rb') as f:
# 		while True:
# 			data = f.readline().decode('gbk')
# 			l = data.split()
# 			print(l)
# 			if not l:
# 				print('遍历结束')
# 				break
# 			elif l[0] == 'word':
# 				print(l[0])

# 				break
# except OSError:
# 	print('文件打开失败')

# b = [b'word', b'n.', b'sound', b'or', b'combination', b'of', b'sounds', b'that', b'expresses', b'a', b'meaning', b'and', b'forms', b'an', b'independent', b'unit', b'of', b'the', b'grammar', b'or', b'vocabulary', b'of', b'a', b'language']
# s = ['word', 'n.', 'sound']

# str = ' '.join(b[1:])

# print(str)

import re

s = "(('poll', datetime.datetime(2018, 8, 5, 23, 28, 18)), ('pool', datetime.datetime(2018, 8, 5, 23, 27, 47)), ('alert', datetime.datetime(2018, 8, 5, 23, 19)), ('select', datetime.datetime(2018, 8, 5, 23, 18, 7)), ('GPS', datetime.datetime(2018, 8, 5, 23, 11, 44)), ('find', datetime.datetime(2018, 8, 5, 23, 10, 46)), ('index', datetime.datetime(2018, 8, 5, 23, 8, 23)), ('index', datetime.datetime(2018, 8, 5, 23, 3, 51)), ('love', datetime.datetime(2018, 8, 5, 22, 9, 24)))"


l = re.findall(r"\(\'.*?\)\)",s)
for i in l:
	print(i)


# l = re.findall(r"\('.*\)\)","(('poll', 'dsds')), ('pool', 'dsfsd')")
# print(l)