import requests
import json

# request.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps({'text': 'lalala'})


json_data = '['
json_data += '{"personnel_id": 2, "first_name": "Chancey", "last_name": "Gardner"},'
json_data += '{"personnel_id": 1, "first_name": "Tom", "last_name": "Clancy"}'
json_data += ']'

json_headers = "'Content-Type': 'application/json'"
url = 'http://127.0.0.1:5000/upsert'


# res = requests.post(url, headers={json_headers}, json=json_parameter)
res = requests.post(url, json=json_data)

if res.ok:
    print(res)
else:
    print(res)
