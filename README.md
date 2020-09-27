# NCU Course to Google Calendar
## Environmental Base on Anaconda 
### Extra module
`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

### Prepare Before Use It
* [Apply Google Calendar api](https://console.developers.google.com/apis/library/calendar-json.googleapis.com)
    1. Download `credentails.json` (From OAUTH Client ID)
    2. Put in the same directory with these file
    3. Replace ${APIKEY} in googlecalender.py with your own api key
* [Apply NCU OAuth Token](https://api.cc.ncu.edu.tw/manage/developer/client/create)
    1. Save Api Token as `api_token`
* Directory 

```
.
├──  .py files(5 files)
├── credentails.json
├── api_token
```
### Using Guide
1. Be Sure about you are in this Directory
1. `python Main.py` 
2. follow the description
3. All Your Class will be update to your Google Calendar