
import requests
import json
btc = []
array = []
inp = 0
i=0
while 1:
    i+=1
    start = input("enter the start date or e to exit:")
    if start == 'e':
         break
    else:
        url = "https://api.coindesk.com/v1/bpi/historical/close.json?start="+ start + "&end=" + start                                                                                    
        response = requests.get(url)
        data = response.text
        #print(data)
        bpi = data.split(":")
        bpi2 = bpi[2]
        bpi3 = bpi2.split("}")
        bpi4 =bpi3[0]
        print(bpi4)
        inp = input('Enter the btc%d: '%i)
        array.append(inp)
        #print(c)
        mul = float(bpi4) * float(inp)
        print(mul)
        btc.append(mul)
        #print (btc)         
        #print (array)
        sum = 0
        sum1 =0
        for b in btc:
            sum = sum + float(b)
            print("sum")
            print("Bitcoin amount:",sum)#bitcoin amount
        for b1 in array:
            sum1 = sum1 + float(b1)
            print("sum1")
            print("Entered value of bitcoins:",sum1)#entered value of the bitcoins
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
usd = (float(USD1) * sum1)-sum
print("Todays price into sum of the btc value minus  total of the btc:",usd)
print("Todays profit in usd:",usd)
url = "https://v3.exchangerate-api.com/bulk/ec270be7fdb11c97eb23d948/USD"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
inr_rate = parsed["rates"]["INR"]
#print(inr_rate)
INRPrice = float(usd) * parsed["rates"]["INR"]
print("Todays profit in INR:",INRPrice)            
        
            
