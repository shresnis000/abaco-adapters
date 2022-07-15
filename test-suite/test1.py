import requests
from tapipy.tapis import Tapis
import os
import time
import timeit
import sys
import json

def basic_response_checks(rsp):
    data = json.loads(rsp.content.decode('utf-8'))
    result = data['result']
    return result

sys.path.append(os.path.split(os.getcwd())[0])
sys.path.append('/actors')
t = Tapis(base_url="https://tacc.develop.tapis.io", username='nshresth', password="")
t.get_tokens()
JWT = t.access_token.access_token


base_url = 'https://localhost:5000'
headers={'X-Tapis-Token':JWT}

start_timer = timeit.default_timer()
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
sent_request = timeit.default_timer()
r4 = requests.get(f'{base_url}/adapters/{reeeee}/data', headers=headers)
got_response = timeit.default_timer()
r5 = requests.delete(f'{base_url}/{reeeee}', headers=headers)
end_timer = timeit.default_timer
time_data = {'total': (end_timer - start_timer) * 1000,
                     'get_response': (got_response - sent_request) * 1000,
                     'initialization': (sent_request - got_response) * 1000,
                     }
print(time_data)
