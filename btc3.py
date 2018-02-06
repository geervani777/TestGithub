import requests
import json

url = " https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=2013-09-05"       
response = requests.get(url)
data = response.text
print(data)



