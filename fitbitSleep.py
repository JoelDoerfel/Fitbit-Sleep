"""ADAPTED FROM: https://towardsdatascience.com/collect-your-own-fitbit-data-with-python-ff145fa10873"""

"""COMMAND LINE"""
"""> python fitbitSleep.py"""

import json

import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd 
import datetime
CLIENT_ID = 'YOUR-CLIENT-ID'
CLIENT_SECRET = 'YOUR-CLIENT-SECRET'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y%m%d"))
today2 = str(datetime.datetime.now().strftime("%Y-%m-%d"))

"""
fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1sec')

time_list = []
val_list = []
for i in fit_statsHR['activities-heart-intraday']['dataset']:
    val_list.append(i['value'])
    time_list.append(i['time'])
heartdf = pd.DataFrame({'Heart Rate':val_list,'Time':time_list})

heartdf.to_csv('C:/{YOUR PATH}/Heart/heartrate-'+ \
                 yesterday+'.csv', \
                 columns=['Time','Heart Rate'], header=True, \
                 index = False)
"""

fit_statsSl = auth2_client.sleep(date='today')

my_data = fit_statsSl
json_data = json.dumps(my_data)
print(json_data)

sdate_list = []
slevel_list = []
ssec_list = []

for i in fit_statsSl['sleep'][0]['levels']['data']:
    sdate_list.append(i['dateTime'])
    slevel_list.append(i['level'])
    ssec_list.append(i['seconds'])
sleepdf = pd.DataFrame({'Time':sdate_list,
                     'Level':slevel_list,
                     'Duration':ssec_list})
sleepdf.to_csv('C:/{YOUR PATH}/SleepStage/sleepStages-' + \
               today+'.csv', \
               columns = ['Time','Level','Duration'],header=True, 
               index = False)
