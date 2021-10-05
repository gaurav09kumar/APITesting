'''
Timeout

Suppose the API is very slow
and after waiting for a particular time we are not getting response

then we want to fail our request

Ex - we are making a payment request

Payment - 30 seconds

If response is not received within 30 seconds then we want to fail request

So we can add a timeout while making a request
'''


import requests

resp = requests.get("https://httpbin.org/delay/3", timeout=5)

print(resp.status_code)
