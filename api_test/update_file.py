import requests
import json

inp_payload = {
    "name": "morpheus",
    "job": "zion resident"
}

inp_payload2 = {
"name": "API",
}
resp = requests.put("https://reqres.in/api/users/2" , data=inp_payload)
# resp2 = requests.put("https://reqres.in/api/users/2" , data=inp_payload2)

# while using put all the properties have to be mentioned
# while using patch we can mention only specific properties that needs to be updated

print(resp)

print(resp.json())

assert resp.json()["job"] == 'zion resident', "Job doesnt match"



