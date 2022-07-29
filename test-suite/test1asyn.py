from asyncio import tasks
import requests
from tapipy.tapis import Tapis
import os
import time
import sys
import json
import statistics
import asyncio
import aiohttp

def basic_response_checks(rsp):
    data = json.loads(rsp.content.decode('utf-8'))
    result = data['result']
    return result

def get_tasks(session,trials,base_url,reeeee,headers):
    tasks = []
    for i in range(trials-1):
        tasks.append(session.get(f'{base_url}/adapters/{reeeee}/data', headers=headers, ssl=False))
    return tasks

async def get_timedata(trials,timedata):
    async with aiohttp.ClientSession() as session:
        for i in range(trials-1):
            tasks = get_tasks(session)
            r4 = await asyncio.gather(*tasks)
            timedata[i] = await (r4[i].elapsed.total_seconds()) * 1000

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
r4=range(trials-1)

asyncio.run(get_timedata(trials,time_data))


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