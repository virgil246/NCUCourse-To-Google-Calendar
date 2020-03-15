import requests
from bs4 import BeautifulSoup
def Query():
    account=input("請輸入帳號: ")
    passwd=input("請輸入密碼: ")
    login_info={"account":account,"passwd":passwd}
    session = requests.Session()
    session.get("https://cis.ncu.edu.tw/Course/main/news/announce")
    r=session.post("https://cis.ncu.edu.tw/Course/main/login",data=login_info)
    r=session.get("https://cis.ncu.edu.tw/Course/main/personal/perCrsstatus")
    s=BeautifulSoup(r.text,"lxml")
    a=s.table.find_all_next("table")[1]
    return a
# with open("output1.html", "w", encoding='utf-8') as file:
#     file.write(str(a))
