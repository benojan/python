import xlrd

index = ['一', '二', '三', '四', '五', '六']
youxiu = 0
lianghao = 0
jige = 0
bujige = 0
for i in index:
	file = '果丽小学'+i+'.xls'
	print(file)
	data = xlrd.open_workbook(file)
	table = data.sheet_by_index(0)
	nrows = table.nrows
	move = 3
	while move < nrows:
		what = table.cell(move, 27).value
		if what == '及格':
			jige += 1
		elif what == '良好':
			lianghao += 1
		elif what == '优秀':
			youxiu += 1
		elif what == '不及格':
			bujige += 1
		elif what == '':
			break
		move += 1
print(youxiu, lianghao, jige, bujige)
