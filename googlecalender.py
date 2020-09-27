import json,requests,datetime

# from __future__ import print_function

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


now_datetime=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
def check(data):
    if data["summary"].find("假開始")!=-1:
        return data
def get_vacation_start_date():
    parm={"key":"${APIKEY}","timeMin":now_datetime.isoformat("T"),"timeMax":(now_datetime+datetime.timedelta(days=6*30)).isoformat("T")}
    resp=requests.get("https://www.googleapis.com/calendar/v3/calendars/ncu.acad@gmail.com/events",params=parm)
    
    data=resp.json()
    # print([item for item in data["items"] if item["summary"].find("暑假開始")]!=-1)
    k=list(filter(check, [item for item in data["items"]]))
    return (k[0]["start"]["date"].replace("-",""))


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)




    


event = {
    'summary': 'Appointment',
    'location': '',
    'start': {
        'dateTime': '2011-06-03T10:00:00.000-07:00',
        'timeZone': 'Asia/Taipei'
    },
    'end': {
        'dateTime': '2011-06-03T10:25:00.000-07:00',
        'timeZone': 'Asia/Taipei'
    },
    'recurrence': [
        'RRULE:FREQ=WEEKLY;UNTIL={20110701T240000Z}',
    ],
    'attendees': [
        # {
        # 'email': 'attendeeEmail',
        # # Other attendee's data...
        # },
        # # ...
    ],
    }

        

def trans_class_to_time(weekday_1,raw):
    d= datetime.datetime.now().date()
    # print(times)

    # print(i)
    weekday=next_weekday(d,int(weekday_1)-1)
    class_start=datetime.datetime.combine(weekday,datetime.time(int(raw[weekday_1][0])+7,0))
    class_end=datetime.datetime.combine(weekday,datetime.time(int(raw[weekday_1][-1])+8,0))
    return class_start,class_end

def upload_event(service_api,data):
    event["recurrence"][0]="RRULE:FREQ=WEEKLY;UNTIL="+get_vacation_start_date()+"T240000Z"
    if input("即將上傳至您的Google Calendar(此為不可逆的操作)是否確定(y/n): ")=="y":
        for i in data:
            event["summary"]=i["課程名稱"]
            for j in i["times"]:
                
                start,end=trans_class_to_time(j,i["times"])
                event["start"]["dateTime"]=start.isoformat()
                event["end"]["dateTime"]=end.isoformat()
                # print(event)
                recurring_event = service_api.events().insert(calendarId='primary', body=event).execute()
                print (recurring_event['id'])

                # create Event

# get_vacation_start_date()
# for j in data[0]["times"]:
        
#         trans_class_to_time(j,data[0]["times"])            

        
# trans_class_to_time(data[0]["times"])    
# print(start.isoformat(),end.isoformat())  

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',"https://www.googleapis.com/auth/calendar.events"
]


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    data={}
    with open("data1.json","r",encoding="utf-8") as file:
        data=json.load(file)
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    upload_event(service,data)
    pass