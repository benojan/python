#装饰器的使用

def head():
	print("headd..........")

def foot():
	print("foott..........")

def head_foot(func):
	def inter():
		head()
		func()
		foot()
	return inter

@head_foot
def page():
	print('content.......')

@head_foot
def page2():
	print('content2.......')

page()
print('------------------------')
page2()