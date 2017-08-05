import requests
from bs4 import BeautifulSoup

params = {
    "userName": "********",
    "password": "********",
}
r = requests.Session()
res = r.post("http://acm.tzc.edu.cn/acmhome/login.do", data=params)

for i in range(1001, 1101):
    params = {
        "userName": "********",
        "problemId": i,
    }

    res = r.get("http://acm.tzc.edu.cn/acmhome/showstatus.do", params=params)

    bs = BeautifulSoup(res.text, "lxml")
    
    link = bs.select(".MYLINE div a")
    if len(link) != 0:
        codeurl = "http://acm.tzc.edu.cn" + link[2].get('href')
        code = r.get(codeurl)
        bs = BeautifulSoup(code.text, "lxml")
        code = bs.select("#code")
        if len(code) != 0:
            print("writing: ", i)
            with open("code/"+str(i)+".txt", 'w', encoding="u8") as f:
                f.write(code[0].text)
