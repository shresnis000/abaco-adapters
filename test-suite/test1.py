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
base_url = 'https://localhost:5000'
JWT = t.access_token.access_token


r = requests.get('http://localhost:5000/adapters', headers={'X-Tapis-Token':JWT})
data = {'image':'nshresth/flask-helloworld'}
r2 = requests.post('http://localhost:5000/adapters', headers={'X-Tapis-Token':JWT}, data=data)
response=basic_response_checks(r2)
reeeee=response['id']
time.sleep(5)
start_timer = timeit.default_timer()
r4 = requests.get(f'http://localhost:5000/adapters/{reeeee}/data', headers={'X-Tapis-Token':JWT})
got_response = timeit.default_timer()

r5 = requests.delete(f'http://localhost:5000/adapters/{reeeee}', headers={'X-Tapis-Token':JWT})