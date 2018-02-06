# passing the two apikeys for the coinbase program
#one for the converting the coinbase
#another for the  indian currency value
import requests

#TODO: Get Input of number of bitcoin


bitcoin = input()
#TODO: Ask Coinbase for price of 1 bitcoin

# These code snippets use an open-source library. http://unirest.io/python
data = requests.get("https://community-coinbase.p.mashape.com/prices/spot_rate?api_key=0972c2cef9274307b25e1b025fadb09b",
  headers={
    "X-Mashape-Key": "Ejm5wx8Wu0mshuTbUpPSGOF0q5QJp1xAMM2jsnwjiWFQv4s6SQ",
    "Accept": "application/json"
  }
)

USDPrice = data.content
print(USDPrice)
import requests
import json

url = "https://v3.exchangerate-api.com/bulk/ec270be7fdb11c97eb23d948/USD"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
inr_rate = parsed["rates"]["INR"]
#print(inr_rate)


#print(c.get_rate('USD', 'INR'))
UP = USDPrice.decode("utf-8")


UP1 = UP.split(":")
UP2 = UP1[1].split(",")

USD = UP2[0]

USD1 = USD.strip('"')
print(USD1)

#TODO: Convert Coinbase USD rate to INR
INRPrice = float(USD1) * parsed["rates"]["INR"]
#TODO: Multiply INR rate with number of bitcoin
print(float(bitcoin)*INRPrice)

#TODO: Print the price
