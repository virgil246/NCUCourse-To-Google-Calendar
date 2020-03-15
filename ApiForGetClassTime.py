import json,requests
def get_class_time(allclass):
    data=allclass
    
    api_token=''
    with open("api_token","r") as file:
        api_token=file.read()
    api_root="https://api.cc.ncu.edu.tw"
    course="/course/v1"
    head={"X-NCU-API-TOKEN":api_token}
    t={}
    for i in data:
        r=requests.get(api_root+course+"/courses/"+i["流水號"],headers=head)
        t=json.loads(r.text)["times"]
        i.update({"times":t})
    with open('data1.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# for i in range(7):
#     try:
#         print(t[str(i)])
#     except:
#         pass
# time+7