__author__ = 'Skoj'
#爬取acm.tzc.edu.com.cn中，帐号下提交的源码
#参考网址：http://www.2cto.com/kf/201305/209931.html

import urllib.request, re
import http.cookiejar
import codecs
import os

#设置cookie
cookie = http.cookiejar.CookieJar()
cookieProc = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookieProc)
urllib.request.install_opener(opener)

#登录帐号
params = {"userName":"xxxxxx", "password":"xxxxxx"}
params = urllib.parse.urlencode(params).encode('gbk')
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0", "Host":"acm.tzc.edu.cn"}
req = urllib.request.Request("http://acm.tzc.edu.cn/acmhome/login.do", data=params, headers=headers)
urllib.request.urlopen(req)

#登录后，获得已做题目列表
req = urllib.request.Request('http://acm.tzc.edu.cn/acmhome/userDetail.do?&userName=benojan', headers=headers)
html = urllib.request.urlopen(req)
html = html.read().decode("gbk")
reg = r'<a href="/acmhome/showstatus\.do\?&userName=benojan&problemId=(\d+)'
reg = re.compile(reg)
pid = re.findall(reg, html)

#遍历题目号对应的提交成功列表
for id in pid:
  #取出提交的代码所对应的编号
	req = urllib.request.Request('http://acm.tzc.edu.cn/acmhome/showstatus.do?userName=benojan&problemId='+id, headers=headers)
	html = urllib.request.urlopen(req)
	html = html.read().decode("gbk")
	reg = r'/acmhome/solutionCode\.do\?id=([\da-z]+)'
	reg = re.compile(reg)
	cid = re.findall(reg, html)
	
	# 读取源代码
	req = urllib.request.Request("http://acm.tzc.edu.cn/acmhome/solutionCode.do?id="+cid[0], headers=headers)
	html = urllib.request.urlopen(req)
	html = html.read().decode("gbk")
	reg = r'readonly>((.|\n)*)</textarea>'
	reg = re.compile(reg)
	code = re.findall(reg, html)
	
	# 将源代码保存到当前程序所在的文件夹下，以题目pid为文件名
	with codecs.open(os.getcwd() + '\\' + id + '.txt','w','utf-8') as f:
		f.write(code[0][0])
