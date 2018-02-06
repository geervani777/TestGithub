import requests
import json
data = requests.get("https://community-coinbase.p.mashape.com/prices/spot_rate?api_key=0972c2cef9274307b25e1b025fadb09b",
    headers={
            "X-Mashape-Key": "Ejm5wx8Wu0mshuTbUpPSGOF0q5QJp1xAMM2jsnwjiWFQv4s6SQ",
            "Accept": "application/json"
}
)
USDPrice = data.content

#print(USDPrice)
UP = USDPrice.decode("utf-8")
UP1 = UP.split(":")
UP2 = UP1[1].split(",")
USD = UP2[0]
USD1 = USD.strip('"')
print( "Todays btc price:",USD1)
url = "https://v3.exchangerate-api.com/bulk/ec270be7fdb11c97eb23d948/USD"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
inr_rate = parsed["rates"]["INR"]
#print(inr_rate)
INRPrice = float(USD1) * parsed["rates"]["INR"]
print("Todays btc in INR:",INRPrice)
btc = input("enter the amount:")
gst = (float(btc)* 18)/100
#print(gst)
fee = (float(btc)*0.75)/100
#print(fee)
#print(gst)
total = float(fee) + float(gst)
#print(total)
bitcoinAmount = float(btc) - float(total)
print(bitcoinAmount)
bitcoinValue = float(bitcoinAmount)/float(INRPrice)
print("bitcoin value of the entered amount:",bitcoinValue)
#if float(btc) <=  10:
    
   #bitcoinValue1 = float(bitcoinValue) * 
   #print( bitcoinValue1)
   
