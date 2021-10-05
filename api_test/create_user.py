#CRUD

#Create - POST

import requests

data_payload = {
    "name": "morpheus",
    "job": "leader"
}

print(type(data_payload))

resp = requests.post("https://reqres.in/api/users", data=data_payload)
print(resp)

print(resp.json())

assert resp.json()['job'] == 'leader', 'Job role doesnt match'


