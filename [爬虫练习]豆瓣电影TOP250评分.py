__author__='Skoj'

import urllib.request, re

def get(url):
    hd = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Host":"movie.douban.com"}

    req = urllib.request.Request(url,headers=hd)
    html = urllib.request.urlopen(req)
    html = html.read().decode("utf-8")

    reg = r'<span class="title">([\s\S]*?)</span>[\s\S]+?<span class="rating_num" property="v:average">([\d\.]+?)</span>'
    reg = re.compile(reg)

    urllist = re.findall(reg, html)
    return urllist

for i in range(10):
    url = 'http://movie.douban.com/top250?start='+str(i*25)
    res = get(url)
    for name,s in res:
        print(count,":",name,":",s)
