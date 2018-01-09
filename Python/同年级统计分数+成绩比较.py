from 统计分数值 import School, Student
import codecs
import os
'''
	1. 显示所有统计信息，一步操作完成
	2. 包含旧年搭基年个成绩比较
	3. 使用方法：
		输入：
			old1.txt ~ old6.txt
			new1.txt ~ new6.txt
			old1格式：
				班级<tab>姓名<tab>学号<tab>（2、3项保留但不参与程序）语文<tab>数学[<tab>英语<tab>科学]
		输出：compare.txt
		
	@author skoj@qq.com
'''

'''
	三~六年级比较函数
'''
def compare(oldSchool, newSchool, filename="compare.txt"):
	with codecs.open(filename,"a","utf-8") as f:		
		classNames = newSchool.allClass()
		classNames.sort()
		if classNames[0] == 31:
			f.write("三年级")
		elif classNames[0] == 41:
			f.write("四年级")
		elif classNames[0] == 51:
			f.write("五年级")
		elif classNames[0] == 61:
			f.write("六年级")
		f.write("\t")
		f.write("班级\t")
		f.write("上学期合格率\t")
		f.write("下学期合格率\t")
		f.write("合格率差值\t")
		f.write("上学期及格率\t")
		f.write("下学期及格率\t")
		f.write("及格率差值\t")
		f.write("上学期优秀率\t")
		f.write("下学期优秀率\t")
		f.write("优秀率差值\t")
		f.write("上学期平均分\t")
		f.write("下学期平均分\t")
		f.write("平均分差值\t")
		f.write("离差值\t")
		f.write("\n")
		
		for kemu in range(4):
			for banji in classNames:
				if kemu == 0:
					f.write("语\t")
				elif kemu == 1:
					f.write("数\t")
				elif kemu == 2:
					f.write("英\t")
				elif kemu == 3:
					f.write("科\t")
				f.write(str(banji) )
				f.write("\t")
				new = newSchool.hegelv(kemu, banji)
				old = oldSchool.hegelv(kemu, banji)
				f.write(str("%.2f%%"%(old*100) ))
				f.write("\t")
				f.write(str("%.2f%%"%(new*100) ))
				f.write("\t")
				f.write(str("%.2f%%"%((new-old)*100) ))
				f.write("\t")
				new = newSchool.jigelv(kemu, banji)
				old = oldSchool.jigelv(kemu, banji)
				f.write(str("%.2f%%"%(old*100) ))
				f.write("\t")
				f.write(str("%.2f%%"%(new*100) ))
				f.write("\t")
				f.write(str("%.2f%%"%((new-old)*100) ))
				f.write("\t")
				new = newSchool.youxiulv(kemu, banji)
				old = oldSchool.youxiulv(kemu, banji)
				f.write(str("%.2f%%"%(old*100) ))
				f.write("\t")
				f.write(str("%.2f%%"%(new*100) ))
				f.write("\t")
				f.write(str("%.2f%%"%((new-old)*100) ))
				f.write("\t")
				new = newSchool.averageBanji(kemu, banji)
				old = oldSchool.averageBanji(kemu, banji)
				f.write(str("%.2f"%old) )
				f.write("\t")
				f.write(str("%.2f"%new) )
				f.write("\t")
				f.write(str("%.2f"%(new-old)) )
				f.write("\t")
				f.write(str("%.2f"%(new-newSchool.average(kemu)) ) )
				f.write("\n")
			f.write("\n")

'''
	三~六年级比较函数2
	因为三年级刚升上来，无法比较英语与科学
'''
def compare_yi(oldSchool, newSchool, filename="compare.txt"):
	with codecs.open(filename,"a","utf-8") as f:		
		classNames = newSchool.allClass()
		classNames.sort()
		if classNames[0] == 31:
			f.write("三年级")
		elif classNames[0] == 41:
			f.write("四年级")
		elif classNames[0] == 51:
			f.write("五年级")
		elif classNames[0] == 61:
			f.write("六年级")
		f.write("\t")
		f.write("班级\t")
		f.write("上学期合格率\t")
		f.write("下学期合格率\t")
		f.write("合格率差值\t")
		f.write("上学期及格率\t")
		f.write("下学期及格率\t")
		f.write("及格率差值\t")
		f.write("上学期优秀率\t")
		f.write("下学期优秀率\t")
		f.write("优秀率差值\t")
		f.write("上学期平均分\t")
		f.write("下学期平均分\t")
		f.write("平均分差值\t")
		f.write("离差值\t")
		f.write("\n")
		
		for kemu in range(4):
			for banji in classNames:
				if kemu == 0:
					f.write("语\t")
				elif kemu == 1:
					f.write("数\t")
				elif kemu == 2:
					f.write("英\t")
				elif kemu == 3:
					f.write("科\t")
				f.write(str(banji) )
				f.write("\t")
				new = newSchool.hegelv(kemu, banji)
				if (banji // 10) == 3 and (kemu == 2 or kemu == 3):	#三年级且学科是英语、科学
					pass
				else:
					old = oldSchool.hegelv(kemu, banji)
					f.write(str("%.2f%%"%(old*100) ))
				f.write("\t")
				f.write(str("%.2f%%"%(new*100) ))
				f.write("\t")
				if (banji // 10) == 3 and (kemu == 2 or kemu == 3):	#三年级且学科是英语、科学
					pass
				else:
					f.write(str("%.2f%%"%((new-old)*100) ))
				f.write("\t")
				new = newSchool.jigelv(kemu, banji)
				if (banji // 10) == 3 and (kemu == 2 or kemu == 3):	#三年级且学科是英语、科学
					pass
				else:
					old = oldSchool.jigelv(kemu, banji)
					f.write(str("%.2f%%"%(old*100) ))
				f.write("\t")
				f.write(str("%.2f%%"%(new*100) ))
				f.write("\t")
				if (banji // 10) == 3 and (kemu == 2 or kemu == 3):	#三年级且学科是英语、科学
					pass
				else:
					f.write(str("%.2f%%"%((new-old)*100) ))
				f.write("\t")
				new = newSchool.youxiulv(kemu, banji)
				if (banji // 10) == 3 and (kemu == 2 or kemu == 3):	#三年级且学科是英语、科学
					pass
				else:
					old = oldSchool.youxiulv(kemu, banji)
					f.write(str("%.2f%%"%(old*100) ))
				f.write("\t")
				f.write(str("%.2f%%"%(new*100) ))
				f.write("\t")
				if (banji // 10) == 3 and (kemu == 2 or kemu == 3):	#三年级且学科是英语、科学
					pass
				else:
					f.write(str("%.2f%%"%((new-old)*100) ))
				f.write("\t")
				new = newSchool.averageBanji(kemu, banji)
				if (banji // 10) == 3 and (kemu == 2 or kemu == 3):	#三年级且学科是英语、科学
					pass
				else:
					old = oldSchool.averageBanji(kemu, banji)
					f.write(str("%.2f"%old) )
				f.write("\t")
				f.write(str("%.2f"%new) )
				f.write("\t")
				if (banji // 10) == 3 and (kemu == 2 or kemu == 3):	#三年级且学科是英语、科学
					pass
				else:
					f.write(str("%.2f"%(new-old)) )
				f.write("\t")
				f.write(str("%.2f"%(new-newSchool.average(kemu)) ) )
				f.write("\n")
			f.write("\n")


def nocompare(newSchool, filename="compare.txt"):
	with codecs.open(filename,"a","u8") as f:
		classNames = newSchool.allClass()
		classNames.sort()
		f.write("一年级")
		f.write("\t")
		f.write("班级\t")
		f.write("上学期合格率\t")
		f.write("下学期合格率\t")
		f.write("合格率差值\t")
		#f.write("及格率\t")
		f.write("上学期优秀率\t")
		f.write("下学期优秀率\t")
		f.write("优秀率差值\t")
		f.write("上学期平均分\t")
		f.write("下学期平均分\t")
		f.write("平均分差值\t")
		f.write("离差值\t")
		f.write("\n")
		for kemu in range(2):
			for banji in classNames:
				if kemu == 0:
					f.write("语\t")
				elif kemu == 1:
					f.write("数\t")
				f.write(str(banji) )
				f.write("\t")
				new = newSchool.hegelv(kemu, banji)
				f.write("\t")
				f.write(str("%.2f%%"%(new*100)) )
				f.write("\t")
				f.write("\t")
				#f.write(str("%.2f%%"%((new-old)*100)) )
				#f.write("\t")
				new = newSchool.jigelv(kemu, banji)
				f.write("\t")
				f.write(str("%.2f%%"%(new*100)) )
				f.write("\t")
				f.write("\t")
				new = newSchool.averageBanji(kemu, banji)
				f.write("\t")
				f.write(str("%.2f"%new) )
				f.write("\t")
				f.write("\t")
				f.write(str("%.2f"%(new-newSchool.average(kemu)) ) )
				f.write("\n")
			f.write("\n")

'''一二年级比较函数'''

def compare12(oldSchool, newSchool, filename="compare.txt"):
	with codecs.open(filename,"a","utf-8") as f:
		
		classNames = newSchool.allClass()
		classNames.sort()
		if classNames[0] == 11:
			f.write("一年级")
		else:
			f.write("二年级")
		f.write("\t")
		f.write("班级\t")
		f.write("上学期合格率\t")
		f.write("下学期合格率\t")
		f.write("合格率差值\t")
		#f.write("及格率\t")
		f.write("上学期优秀率\t")
		f.write("下学期优秀率\t")
		f.write("优秀率差值\t")
		f.write("上学期平均分\t")
		f.write("下学期平均分\t")
		f.write("平均分差值\t")
		f.write("离差值\t")
		f.write("\n")
		for kemu in range(2):
			for banji in classNames:
				if kemu == 0:
					f.write("语\t")
				elif kemu == 1:
					f.write("数\t")
				f.write(str(banji) )
				f.write("\t")
				new = newSchool.hegelv(kemu, banji)
				old = oldSchool.hegelv(kemu, banji)
				f.write(str("%.2f%%"%(old*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(new*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%((new-old)*100)) )
				f.write("\t")
				#f.write(str("%.2f%%"%((new-old)*100)) )
				#f.write("\t")
				new = newSchool.jigelv(kemu, banji)
				old = oldSchool.jigelv(kemu, banji)
				f.write(str("%.2f%%"%(old*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(new*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%((new-old)*100)) )
				f.write("\t")
				new = newSchool.averageBanji(kemu, banji)
				old = oldSchool.averageBanji(kemu, banji)
				f.write(str("%.2f"%old) )
				f.write("\t")
				f.write(str("%.2f"%new) )
				f.write("\t")
				f.write(str("%.2f"%(new-old)) )
				f.write("\t")
				f.write(str("%.2f"%(new-newSchool.average(kemu)) ) )
				f.write("\n")
			f.write("\n")
			
			
'''程序开始'''
new = School()	#用于存放学生成绩信息
old = School()
for i in range(1,7):	#遍历所有年级
	new.clear()
	old.clear()
	if i < 3:	#一二年级
		if i == 1:
			with codecs.open("new"+str(i)+".txt", "r", "u8") as f:
				lines = f.readlines()
				for line in lines:
					banji, xuehao, xingming, yuwen, shuxue = line.split("\t")
					s = Student(int(banji), float(yuwen), float(shuxue))
					new.add(s)
			nocompare(new)
			continue
		#读入上下学期成绩
		with codecs.open("old"+str(i)+".txt", "r", "u8") as f:
			lines = f.readlines()
			for line in lines:
				banji, xuehao, xingming, yuwen, shuxue = line.split("\t")
				s = Student(int(banji), float(yuwen), float(shuxue))
				old.add(s)
				
		with codecs.open("new"+str(i)+".txt", "r", "u8") as f:
			lines = f.readlines()
			for line in lines:
				banji, xuehao, xingming, yuwen, shuxue = line.split("\t")
				s = Student(int(banji), float(yuwen), float(shuxue))
				new.add(s)
		#调用比较函数
		compare12(old, new)
	else:	#三~六年级
		#读入上下学期成绩
		with codecs.open("old"+str(i)+".txt", "r", "u8") as f:
			lines = f.readlines()
			for line in lines:
				print(line)
				if i != 3:
					banji, xuehao, xingming, yuwen, shuxue, yingyu, kexue = line.split("\t")
					s = Student(int(banji), float(yuwen), float(shuxue), float(yingyu), float(kexue))
				else:
					banji, xuehao, xingming, yuwen, shuxue = line.split("\t")
					s = Student(int(banji), float(yuwen), float(shuxue))
				old.add(s)
				
		with codecs.open("new"+str(i)+".txt", "r", "u8") as f:
			lines = f.readlines()
			for line in lines:
				print(line)
				banji, xuehao, xingming, yuwen, shuxue, yingyu, kexue = line.split("\t")
				s = Student(int(banji), float(yuwen), float(shuxue), float(yingyu), float(kexue))
				new.add(s)
		#调用比较函数
		compare_yi(old, new)
