import requests
import json
start = input("enter the start date:")
url = "https://api.coindesk.com/v1/bpi/historical/close.json?start="+ start + "&end=" + start                                                                                    
response = requests.get(url)
data = response.text
print(data)
bpi = data.split(":")
bpi2 = bpi[2]
bpi3 = bpi2.split("}")
bpi4 =bpi3[0]
print(bpi4)

