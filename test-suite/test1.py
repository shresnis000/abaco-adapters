import requests
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
JWT = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJiODQyMTg5OS05MTYzLTRiYWQtOTcxZS0wZmU2MmU1MWFmNDEiLCJpc3MiOiJodHRwczovL2Rldi5kZXZlbG9wLnRhcGlzLmlvL3YzL3Rva2VucyIsInN1YiI6InRlc3R1c2VyMkBkZXYiLCJ0YXBpcy90ZW5hbnRfaWQiOiJkZXYiLCJ0YXBpcy90b2tlbl90eXBlIjoiYWNjZXNzIiwidGFwaXMvZGVsZWdhdGlvbiI6ZmFsc2UsInRhcGlzL2RlbGVnYXRpb25fc3ViIjpudWxsLCJ0YXBpcy91c2VybmFtZSI6InRlc3R1c2VyMiIsInRhcGlzL2FjY291bnRfdHlwZSI6InVzZXIiLCJleHAiOjE2NTkxNDA4NjksInRhcGlzL2NsaWVudF9pZCI6bnVsbCwidGFwaXMvZ3JhbnRfdHlwZSI6InBhc3N3b3JkIn0.fHxKP3xrLcaVrOx3jrhm833qC7njabyA5GXyS2u0ClvwaeXrryTaMfyzMa81eQrx-2hrqt5SNnm-DhzjKPAYps72hirLYKNHLGnQfBmMKhxx-JJYb5d4Qd0xLbKbG8tDq4lLH8unsognyZKwss2iDypoUrs2bCkQV9jsz-lMv0ldEWYG14-etrWf451WlCxF2RyoxdmE9nF-t59qMPhUFt11KUCnYKQjaxz8Z05ctc9aU6q13m8FZJcIjHSZcgu-EyzrwZq80IJhuj_nKce0jJx8eq2KKrHn8AOz-EmPGs3S6ifHsIB2nC9iAgL4MUtzNOMZyvsVDNkhjPhg54Od4g'


base_url = 'https://localhost:8000'
headers={'X-Tapis-Token':JWT}


data = {'image':'nshresth/flask-helloworld'}

r1 = requests.get('http://localhost:8000/actors', headers=headers)

print(r1.content)
