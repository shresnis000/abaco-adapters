import requests
from tapipy.tapis import Tapis
import os
import time
import timeit
import sys
import json
import statistics

def basic_response_checks(rsp):
    data = json.loads(rsp.content.decode('utf-8'))
    result = data['result']
    return result

sys.path.append(os.path.split(os.getcwd())[0])
sys.path.append('/actors')
t = Tapis(base_url="https://tacc.develop.tapis.io", username='nshresth', password="")
t.get_tokens()
JWT = t.access_token.access_token


base_url = 'https://localhost:8000'
headers={'X-Tapis-Token':JWT}


data = {'image':'nshresth/flask-helloworld'}
r2 = requests.post(f'{base_url}/adapters', headers=headers, data=data)
response=basic_response_checks(r2)
reeeee=response['id']
while idx<20 and not success:
        try:
            rsp = requests.get(f'{base_url}/data', headers=headers)
            result = basic_response_checks(rsp)
            success=True
        except:
            time.sleep(1)
            idx = idx + 1

trials=100
time_data=range(trials-1)
time_stats={}
for i in range(trials-1):
    r4 = requests.get(f'{base_url}/adapters/{reeeee}/data', headers=headers)
    time_data[i] = (r4.elapsed.total_seconds()) * 1000

#number of calls made
time_stats['n']=trials
#median
time_stats['median']=statistics.median(time_data)
#mean
time_stats['mean']=statistics.mean(time_data)
#standard deviation
time_stats['standard deviation']=statistics.pstdev(time_data)
#max
time_stats['max']=max(time_data)
#min
time_stats['min']=min(time_data)

r5 = requests.delete(f'{base_url}/{reeeee}', headers=headers)
print(time_stats)
