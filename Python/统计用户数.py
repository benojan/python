import codecs

'''
# uv.txt 中数据内容范例
时间 用户号 操作
2015-08-24_00:00:00 55311 buy
2015-08-24_00:00:01 73069 add2cart
2015-08-24_00:00:02 62843 add2cart
2015-08-24_00:00:03 14187 search
2015-08-24_00:00:04 77895 pay
2015-08-24_00:00:05 81708 pay
2015-08-24_00:00:06 67010 add2cart
'''
with codecs.open("C:\\Users\\Administrator\\Desktop\\uv.txt",'r',"u8") as f:
	lines = f.readlines()
	usrs = {}
	for line in lines:
		time, usr, thing = line.split(' ')
		usrs[usr] = usr
	print(len(usrs))
