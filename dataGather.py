import os
import requests

BaseQueryUrl = "https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&make={}&model={}"
make = 'ford'
model = 'mustang'

r = requests.get(BaseQueryUrl.format(make, model))
print(r.text)
