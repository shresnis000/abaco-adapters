import requests
import os
import time
import sys
import json


def basic_response_checks(rsp):
    data = json.loads(rsp.content.decode('utf-8'))
    result = data['result']
    return result

sys.path.append(os.path.split(os.getcwd())[0])
sys.path.append('/actors')
JWT = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJiODQyMTg5OS05MTYzLTRiYWQtOTcxZS0wZmU2MmU1MWFmNDEiLCJpc3MiOiJodHRwczovL2Rldi5kZXZlbG9wLnRhcGlzLmlvL3YzL3Rva2VucyIsInN1YiI6InRlc3R1c2VyMkBkZXYiLCJ0YXBpcy90ZW5hbnRfaWQiOiJkZXYiLCJ0YXBpcy90b2tlbl90eXBlIjoiYWNjZXNzIiwidGFwaXMvZGVsZWdhdGlvbiI6ZmFsc2UsInRhcGlzL2RlbGVnYXRpb25fc3ViIjpudWxsLCJ0YXBpcy91c2VybmFtZSI6InRlc3R1c2VyMiIsInRhcGlzL2FjY291bnRfdHlwZSI6InVzZXIiLCJleHAiOjE2NTkxNDA4NjksInRhcGlzL2NsaWVudF9pZCI6bnVsbCwidGFwaXMvZ3JhbnRfdHlwZSI6InBhc3N3b3JkIn0.fHxKP3xrLcaVrOx3jrhm833qC7njabyA5GXyS2u0ClvwaeXrryTaMfyzMa81eQrx-2hrqt5SNnm-DhzjKPAYps72hirLYKNHLGnQfBmMKhxx-JJYb5d4Qd0xLbKbG8tDq4lLH8unsognyZKwss2iDypoUrs2bCkQV9jsz-lMv0ldEWYG14-etrWf451WlCxF2RyoxdmE9nF-t59qMPhUFt11KUCnYKQjaxz8Z05ctc9aU6q13m8FZJcIjHSZcgu-EyzrwZq80IJhuj_nKce0jJx8eq2KKrHn8AOz-EmPGs3S6ifHsIB2nC9iAgL4MUtzNOMZyvsVDNkhjPhg54Od4g'


base_url = 'https://localhost:8000'
headers={'X-Tapis-Token':JWT}


data = {'image':'nshresth/flask-helloworld'}
r2 = requests.post(f'{base_url}/adapters', headers=headers, data=data)
response=basic_response_checks(r2)
reeeee=response['id']
idx=0
success=False
while idx<20 and not success:
        try:
            rsp = requests.get(f'{base_url}/data', headers=headers)
            result = basic_response_checks(rsp)
            success=True
        except:
            time.sleep(1)
            idx = idx + 1

trials=3
time_data=list(range(trials-1))
time_stats={}
for i in range(trials-1):
    r4 = requests.get(f'{base_url}/adapters/{reeeee}/data', headers=headers)

r5= requests.get(f'http://localhost:5000/adapters/{reeeee}/logs', headers={'X-Tapis-Token':JWT})
Time_breakdowns=basic_response_checks(r5)
listy={'got_adapter':[],'got_server':[],'got_address':[],'got_decoded':[],'got_headers':[],'got_response':[],'total':[]}
for i in Time_breakdowns:
    listy['got_adapter'].append(i['get_adapter'])
    listy['got_address'].append(i['got_address'])
    listy['got_decoded'].append(i['got_decoded'])
    listy['got_headers'].append(i['got_headers'])
    listy['got_response'].append(i['got_response'])
    listy['got_server'].append(i['got_server'])
    listy['total'].append(i['total'])
for j in listy:
    #number of calls made
    time_stats['n']=trials
    #median
    time_stats['median']=statistics.median(listy[j])
    #mean
    time_stats['mean']=statistics.mean(listy[j])
    #standard deviation
    time_stats['standard deviation']=statistics.pstdev(listy[j])
    #max
    time_stats['max']=max(listy[j])
    #min
    time_stats['min']=min(listy[j])
    print(j)
    print(time_stats)
    print('\n')

r5 = requests.delete(f'{base_url}/{reeeee}', headers=headers)