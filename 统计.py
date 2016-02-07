import codecs

with codecs.open("C:\\Users\\Administrator\\Desktop\\uv.txt",'r',"u8") as f:
	lines = f.readlines()
	usrs = {}
	for line in lines:
		time, usr, thing = line.split(' ')
		usrs[usr] = usr
	print(len(usrs))
