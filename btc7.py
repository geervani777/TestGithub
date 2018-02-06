import requests
import json
array = []
array1 = []
while True:
    
    data = requests.get("https://community-coinbase.p.mashape.com/prices/spot_rate?api_key=a76e4cded477438f8210093657159182",
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
    print( "Todays btc price :",USD1)
    
    url = "https://v3.exchangerate-api.com/bulk/ec270be7fdb11c97eb23d948/USD"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    inr_rate = parsed["rates"]["INR"]
    #print(inr_rate)
    INRPrice = float(USD1) * parsed["rates"]["INR"]
    print("Todays btc in INR:",INRPrice)
    start = input("Enter the start date :")
    url = "https://api.coindesk.com/v1/bpi/historical/close.json?start="+ start + "&end=" + start                                                                                    
    response = requests.get(url)
    data = response.text
    #print(data)
    bpi = data.split(":")
    bpi2 = bpi[2]
    bpi3 = bpi2.split("}")
    bpi4 =bpi3[0]
    print(bpi4)
    INRprice1 = float(bpi4) * parsed["rates"]["INR"]
    print("Enter date btc amount in INR:",INRprice1)
    
    btc = input("Enter the amount or e to exit:")
    if btc == 'e':
         break
    else:
        #btc1 = float(btc)/float(add)
        #print(btc1)
        gst = (float(btc)* 18)/100
        fee = (float(btc)*0.75)/100
        #print(gst)
        #print(fee)
        total = float(fee) + float(gst)
        bitcoinPurchasingPrice = float(btc) - total
        #print(bitcoinPurchasingPrice )
        array1.append(bitcoinPurchasingPrice)
        #print( array1)
        bitcoinValue = float(bitcoinPurchasingPrice)/float(INRprice1)
        print("Bitcoin value of the entered amount:", bitcoinValue)
        array.append(bitcoinValue)
        #print(c)
        sum = 0
        sum1 = 0
        for amount in array:
            sum = sum + float(amount)
            print("sum")
            print("Adding the bitcoin purchasing value:",sum)#bitcoin purchasing value
        for amount1 in array1:
            sum1 = sum1 + float(amount1)
            print("sum1")
            print("Adding the bitcoin purchasing amount:",sum1)#btc purchasing amount
multiplay =  float(INRPrice) * float(sum)
#print( "Today price into bitcoinPurchasingPrice value:",multiplay)
profit = float(multiplay ) - float(sum1)
print( "Todays profit:",profit)

                


