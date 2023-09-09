"""ADAPTED FROM: https://towardsdatascience.com/collect-your-own-fitbit-data-with-python-ff145fa10873"""

"""COMMAND LINE"""
"""> python fitbitSleep.py"""

import json

import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd 
import datetime

from dev_secrets.fitbit_creds import fitbit_client_id, fitbit_client_secret

CLIENT_ID = fitbit_client_id
CLIENT_SECRET = fitbit_client_secret

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y%m%d"))
today2 = str(datetime.datetime.now().strftime("%Y-%m-%d"))

def intraday_hr(file_path):
    fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1sec')

    date_list = []
    time_list = []
    val_list = []
    for i in fit_statsHR['activities-heart-intraday']['dataset']:
        date_list.append(str(yesterday2))
        val_list.append(i['value'])
        time_list.append(i['time'])
    heartdf = pd.DataFrame({'Date':date_list,'Time':time_list,'Heart Rate':val_list})

    folder = 'Intraday_HR/'
    file_name = 'intraday_hr_'+yesterday+'.csv'
    heartdf.to_csv(file_path+folder+file_name, \
                    columns=['Date','Time','Heart Rate'], header=True, \
                    index = False)

    #return heartdf                    

def sleep_stages(file_path):
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

    folder = 'Sleep_Stages/'
    file_name = 'sleepStages_'+yesterday+'.csv'

    sleepdf.to_csv(file_path+folder+file_name, 
                columns = ['Date','Time','Level','Duration'], 
                header=True, 
                index = False)

    #return sleepdf

def main():
    file_path = 'C:/Users/Admin/Documents/Fitbit/'
    intraday_hr(file_path)
    #sleep_stages(file_path)

main()