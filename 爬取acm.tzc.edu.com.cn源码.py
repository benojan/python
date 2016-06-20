__author__ = 'Skoj'
#爬取acm.tzc.edu.com.cn中，帐号下提交的源码

import urllib.request, re

def getCodeUrl(url):
  hd = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0", "Host":"acm.tzc.edu.cn"}
  req = urllib.request.Request(url,headers=hd)
  html = urllib.request.urlopen(req)
  html = html.read().decode("GB2312")
  reg = r'<a href="/acmhome/solutionCode\.do\?id=([\da-z]+)'
  reg = re.compile(reg)
  urllist = re.findall(reg, html)
  return urllist

def get(url):
  hd = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0", "Host":"acm.tzc.edu.cn"}
  req = urllib.request.Request(url,headers=hd)
  html = urllib.request.urlopen(req)
  html = html.read().decode("GB2312")
  reg = r'<a href="/acmhome/showstatus\.do\?&userName=benojan&problemId=(\d+)'
  reg = re.compile(reg)	
  urllist = re.findall(reg, html)
  return urllist

url = 'http://acm.tzc.edu.cn/acmhome/userDetail.do?&userName=benojan'
res = get(url)
for key in res:
  print('start')
  url = 'http://acm.tzc.edu.cn/acmhome/showstatus.do?&userName=benojan&problemId='+key
  res1 = getCodeUrl(url)
  for key1 in res1:
    print(key1)
