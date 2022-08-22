import requests
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
JWT = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJjZGMyN2UyNy00NGMxLTQ1N2QtYWNhZi0yMTE1ZDE3NWQ1NGEiLCJpc3MiOiJodHRwczovL2Rldi5kZXZlbG9wLnRhcGlzLmlvL3YzL3Rva2VucyIsInN1YiI6InRlc3R1c2VyMkBkZXYiLCJ0YXBpcy90ZW5hbnRfaWQiOiJkZXYiLCJ0YXBpcy90b2tlbl90eXBlIjoiYWNjZXNzIiwidGFwaXMvZGVsZWdhdGlvbiI6ZmFsc2UsInRhcGlzL2RlbGVnYXRpb25fc3ViIjpudWxsLCJ0YXBpcy91c2VybmFtZSI6InRlc3R1c2VyMiIsInRhcGlzL2FjY291bnRfdHlwZSI6InVzZXIiLCJleHAiOjE2NjAxNzA0MjYsInRhcGlzL2NsaWVudF9pZCI6bnVsbCwidGFwaXMvZ3JhbnRfdHlwZSI6InBhc3N3b3JkIn0.I_0cENXMbyLIzNSCApCdqYpLJXI-yJdnXOww248rHoET0P2AHBMTwahI3ariy90DV_rhi4ahUH7f612JUOZPyIlJ2_6HpzbjdmtRAO1a2Cu4YIgd--VazaDwjmardNp7w1cMvAM5NcSSe2ByguQLEEzhqHMa-OAPsdk5sXRmKip11s2zWgr4zZaIFuQ1YI9BsP3iaQPTcXn6--hHr5AHfAPERmDZ60LijFZ4YeUGNPmRKgNuVc7nOThvGZY_xIB1U74h6QJOrx30DinlU19OSDvGmfYQvNrorfpAElSc51vTCDz0d3dXY_t_HjVAD-PR_8ix1bm1dpTC_tdLu23_0w"

base_url = 'http://localhost:8000'
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

trials=10
time_data=list(range(trials-1))
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
