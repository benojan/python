import codecs

#学生类
class Student:
	def __init__(self,banji,yuwen,shuxue,yingyu=0,kexue=0):
		self.banji = banji
		self.yuwen = yuwen
		self.shuxue = shuxue
		self.yingyu = yingyu
		self.kexue = kexue
	def banji(self):
		return self.banji
	def yuwen(self):
		return self.yuwen
	def shuxue(self):
		return self.shuxue
	def yingyu(self):
		return self.yingyu
	def kexue(self):
		return self.kexue

#学校类
class School:
	
	def __init__(self):
		self.students = []	#学生列表
	
	def clear(self):	#清除学生列表
		self.students.clear()
	def add(self, s):	#添加学生
		self.students.append(s)
		
	def num(self):	#返回学生数
		return len(self.students)
		
	def numBanji(self, banji):	#返回班级人数
		cnt = 0
		for student in self.students:
			if student.banji == banji:
				cnt += 1
		return cnt
		
	def average(self, kemu):	#科目全校平均分
		score = 0
		for student in self.students:
			if kemu == 0:
				score += student.yuwen
			elif kemu == 1:
				score += student.shuxue
			elif kemu == 2:
				score += student.yingyu
			elif kemu == 3:
				score += student.kexue
		return score / len(self.students)
	
	def averageBanji(self, kemu, banji):	#科目班级平均分
		score = 0
		cnt = 0
		for student in self.students:
			if student.banji == banji:
				if kemu == 0:
					score += student.yuwen
				elif kemu == 1:
					score += student.shuxue
				elif kemu == 2:
					score += student.yingyu
				elif kemu == 3:
					score += student.kexue
				cnt += 1
		return score / cnt
		
	def hege(self, kemu):	#科目全校合格分
		scores = []
		for student in self.students:
			if kemu == 0:
				scores.append(student.yuwen)
			elif kemu == 1:
				scores.append(student.shuxue)
			elif kemu == 2:
				scores.append(student.yingyu)
			elif kemu == 3:
				scores.append(student.kexue)
		scores.sort(reverse = False)
		base = int(len(scores)*0.2)
		number = scores[base-1]
		return number
		
	def hegelv(self, kemu, banji):	#科目班级合格率
		cnt = 0
		cnt1 = 0
		hegeScore = 80 if banji < 30 else self.hege(kemu)	#1、2年级80分，3~6年级80%
		for student in self.students:
			if student.banji == banji:
				if kemu == 0:
					if student.yuwen >= hegeScore:
						cnt += 1
				elif kemu == 1:
					if student.shuxue >= hegeScore:
						cnt += 1
				elif kemu == 2:
					if student.yingyu >= hegeScore:
						cnt += 1
				elif kemu == 3:
					if student.kexue >= hegeScore:
						cnt += 1
				cnt1 += 1
		return cnt/cnt1
	
	def jigelv(self, kemu, banji):	#科目班级合格率
		normalScore = 60
		cnt = 0
		cnt1 = 0
		for student in self.students:
			if student.banji == banji:
				cnt1 += 1	#班级人数
				#每门科目合格人数
				if kemu == 0:
					if student.yuwen >= normalScore:
						cnt += 1
				elif kemu == 1:
					if student.shuxue >= normalScore:
						cnt += 1
				elif kemu == 2:
					if student.yingyu >= (70*0.6):
						cnt += 1
				elif kemu == 3:
					if student.kexue >= normalScore:
						cnt += 1
		return cnt/cnt1
		
	def youxiulv(self, kemu, banji):	#科目班级优秀率
		highscore = 90 if banji < 30 else 85	#1、2年级90分，3~6年级85分
		cnt = 0
		cnt1 = 0
		for student in self.students:
			if student.banji == banji:
				cnt1 += 1
				if kemu == 0:
					if student.yuwen >= highscore:
						cnt += 1
				elif kemu == 1:
					if student.shuxue >= highscore:
						cnt += 1
				elif kemu == 2:
					if student.yingyu >= (70*0.85):
						cnt += 1
				elif kemu == 3:
					if student.kexue >= highscore:
						cnt += 1
		return cnt/cnt1
	def allClass(self):
		classNames = []
		for student in self.students:
			if student.banji not in classNames:
				classNames.append(student.banji)
		return classNames
	
	def out(self, filename="result.txt"):	#输出3~6年级
		with codecs.open(filename,"w","utf-8") as f:
			f.write("合格分\t")
			f.write(str(self.hege(0)) )
			f.write("\t")
			f.write(str(self.hege(1)) )
			f.write("\t")
			f.write(str(self.hege(2)) )
			f.write("\t")
			f.write(str(self.hege(3)) )
			f.write("\n")
			
			f.write("平均分\t")
			f.write(str("%.2f"%self.average(0)) )
			f.write("\t")
			f.write(str("%.2f"%self.average(1)) )
			f.write("\t")
			f.write(str("%.2f"%self.average(2)) )
			f.write("\t")
			f.write(str("%.2f"%self.average(3)) )
			f.write("\n")
			f.write("\n")
			
			f.write("\t")
			f.write("班级\t")
			f.write("合格率(按百分比)\t")
			f.write("及格率\t")
			f.write("优秀率\t")
			f.write("平均分\t")
			f.write("离差值")
			f.write("\n")
			
			classNames = self.allClass()
			classNames.sort()
			for banji in classNames:
				f.write("语\t")
				f.write(str(banji) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.hegelv(0, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.jigelv(0, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.youxiulv(0, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f"%self.averageBanji(0, banji)) )
				f.write("\t")
				f.write(str("%.2f"%(self.averageBanji(0,banji)-self.average(0)) ) )
				f.write("\n")
			f.write("\n")
			
			for banji in classNames:
				f.write("数\t")
				f.write(str(banji) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.hegelv(1, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.jigelv(1, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.youxiulv(1, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f"%self.averageBanji(1, banji)) )
				f.write("\t")
				f.write(str("%.2f"%(self.averageBanji(1,banji)-self.average(1)) ) )
				f.write("\n")
			f.write("\n")
			
			for banji in classNames:
				f.write("英\t")
				f.write(str(banji) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.hegelv(2, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.jigelv(2, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.youxiulv(2, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f"%self.averageBanji(2, banji)) )
				f.write("\t")
				f.write(str("%.2f"%(self.averageBanji(2,banji)-self.average(2)) ) )
				f.write("\n")
			f.write("\n")
			
			for banji in classNames:
				f.write("科\t")
				f.write(str(banji) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.hegelv(3, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.jigelv(3, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.youxiulv(3, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f"%self.averageBanji(3, banji)) )
				f.write("\t")
				f.write(str("%.2f"%(self.averageBanji(3,banji)-self.average(3)) ) )
				f.write("\n")
	def out12(self, filename="result.txt"):	#输出1、2年级
		with codecs.open(filename,"w","utf-8") as f:
			f.write("平均分\t")
			f.write(str("%.2f"%self.average(0)) )
			f.write("\t")
			f.write(str("%.2f"%self.average(1)) )
			f.write("\n")
			f.write("\n")
			
			f.write("\t")
			f.write("班级\t")
			f.write("合格率\t")
			#f.write("及格率\t")
			f.write("优秀率\t")
			f.write("平均分\t")
			f.write("离差值")
			f.write("\n")
			
			classNames = self.allClass()
			classNames.sort()
			for banji in classNames:
				f.write("语\t")
				f.write(str(banji) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.hegelv(0, banji)*100)) )
				f.write("\t")
				#f.write(str("%.2f%%"%(self.jigelv(0, banji)*100)) )
				#f.write("\t")
				f.write(str("%.2f%%"%(self.youxiulv(0, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f"%self.averageBanji(0, banji)) )
				f.write("\t")
				f.write(str("%.2f"%(self.averageBanji(0,banji)-self.average(0)) ) )
				f.write("\n")
			f.write("\n")
			
			for banji in classNames:
				f.write("数\t")
				f.write(str(banji) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.hegelv(1, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.jigelv(1, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f%%"%(self.youxiulv(1, banji)*100)) )
				f.write("\t")
				f.write(str("%.2f"%self.averageBanji(1, banji)) )
				f.write("\t")
				f.write(str("%.2f"%(self.averageBanji(1,banji)-self.average(1)) ) )
				f.write("\n")
			f.write("\n")
