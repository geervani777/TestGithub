import requests
import json
url = "https://www.throughbit.com/tbit_ci/index.php/cryptoprice/type/BTC/INR"
response = requests.get(url)
data = response.content
#print(data)
INRprice = data.decode("utf-8")
INR1 = INRprice.split('{')
INR2 = INR1[3]
INR3 = INR2.split('}')
INR4 = INR3[0]
print("bitcoin buying and selling price in troughbit")
print(INR4)

print("coinBase bitCoin buying price in USD")
data = requests.get("https://community-coinbase.p.mashape.com/prices/buy?api_key=WuHXU1O17qLCzsoI",
  headers={
    "X-Mashape-Key": "Ejm5wx8Wu0mshuTbUpPSGOF0q5QJp1xAMM2jsnwjiWFQv4s6SQ",
    "Accept": "application/json"
  }
)
USDPrice = data.content
#print(USDPrice)
UP = USDPrice.decode("utf-8")


UP1 = UP.split(":")
UP2 = UP1[20].split(",")

USD = UP2[0]

USD1 = USD.strip('"')
print(USD1)
print("coinBase bitCoin selling price in USD")
data = requests.get("https://community-coinbase.p.mashape.com/prices/sell?api_key=WuHXU1O17qLCzsoI",
  headers={
    "X-Mashape-Key": "Ejm5wx8Wu0mshuTbUpPSGOF0q5QJp1xAMM2jsnwjiWFQv4s6SQ",
    "Accept": "application/json"
  }
)
USDPrice1 = data.content
#print(USDPrice1)
UP = USDPrice1.decode("utf-8")


UP1 = UP.split(":")
UP2 = UP1[20].split(",")

USD = UP2[0]

USD1 = USD.strip('"')
print(USD1)
url = "https://koinex.in/api/ticker"
response = requests.get(url)
data = response.content
#print(data)
INRprice = data.decode("utf-8")
INR1 = INRprice.split('{')
INR2 = INR1[5]
INR3 = INR2.split(',')
INR4 = INR3[0]
print("bitcoin buying and selling price in koinex")
print(INR4)

