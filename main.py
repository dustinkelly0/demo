import requests 

payload = {'username': 'dustin', 'password': 'password'}
url = "https://httpbin.org/post"

req = requests.post(url, data=payload)

req_dict = req.json()

print(req_dict['form'])
