import requests 
import json
import pandas as pd

participants =  pd.read_csv('C:/Users/rajat/gen-certificate/participant_list.csv')
URL = "http://localhost:8000/participant/"
for i in range(len(participants)):
    data = {'name': participants.iloc[i]['name'],
            'email': participants.iloc[i]['email'],
            'gender':  participants.iloc[i]['gender'],
           }
    data_json = json.dumps(data)
    r = requests.post(URL,data=data_json,verify=False)