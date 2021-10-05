import json

import requests


my_data = open("data.json", "r").read()

resp = requests.post("https://reqres.in/api/users", data=json.loads(my_data))


print(resp)

print(resp.json())

print(resp.headers.get("Content-Type"))
assert resp.json()['job'] == 'Automation', 'Job role doesnt match'


