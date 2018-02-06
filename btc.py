import requests

import requests
import json
while True:
    date = input("enter the date:")
    btc = input("enter the btc:")
    price = input("enter the price:")
    a = input("Another one? yes/no > ").lower()
    
    if a=="y":
        date()
        btc()
        price()
        continue
    elif a=="no":
        data = requests.get("https://community-coinbase.p.mashape.com/prices/spot_rate?api_key=0972c2cef9274307b25e1b025fadb09b",
        headers={
        "X-Mashape-Key": "Ejm5wx8Wu0mshuTbUpPSGOF0q5QJp1xAMM2jsnwjiWFQv4s6SQ",
        "Accept": "application/json"
        }
        )

        USDPrice = data.content
#print(USDPrice)
        url = "https://v3.exchangerate-api.com/bulk/ec270be7fdb11c97eb23d948/USD"
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)
        inr_rate = parsed["rates"]["INR"]
#print(inr_rate)
        UP = USDPrice.decode("utf-8")
        UP1 = UP.split(":")
        UP2 = UP1[1].split(",")
        USD = UP2[0]
        USD1 = USD.strip('"')
        btc1 = float(USD1)  * float( btc)
        INRPrice = float(btc1) * parsed["rates"]["INR"]
        print('what is the price to day?',INRPrice)
        amount = float( INRPrice) - float(price)
        print(amount)
        break
 
    
