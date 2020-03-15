import json,requests

from bs4 import BeautifulSoup as bs

from ApiForGetClassTime import get_class_time



soup=bs(open("output1.html",encoding="utf-8"),"lxml")
def parse_to_json(soup):
    col =soup.find_all('tr')
    title=[]
    for i in col[0].find_all('th')[1:-3]:
        title.append(i.get_text().strip())


    allclass=[]
    for i in col[2:-1]:
        clas=[]
        for j in i.find_all("td")[1:7]:
            clas.append(j.get_text().strip())
        # print(clas)
        finalclas={}
        for k in range(6):
            finalclas.update({title[k]:clas[k]})
        # print(finalclas)
        allclass.append(finalclas)

    # for i in range(6):
    #     finalclas.update({title[i]:clas[i]})
    credit=sum([int(item["學分"]) for item in allclass])
    print ("堂數: "+str(len(allclass)) )
    print("學分: "+ str(credit))

    if input("這樣正確嗎(y/n)")=="y":
        # with open('data.json', 'w', encoding='utf-8') as f:
        #     json.dump(allclass, f, ensure_ascii=False, indent=4)
        get_class_time(allclass)
        pass