from forex_python.converter import CurrencyRates
c = CurrencyRates()
import requests
import json
# These code snippets use an open-source library. http://unirest.io/python
data = requests.get("https://community-coinbase.p.mashape.com/prices/spot_rate?api_key=0pZBzyoR5RSvUsAs",
  headers={
    "X-Mashape-Key": "Ejm5wx8Wu0mshuTbUpPSGOF0q5QJp1xAMM2jsnwjiWFQv4s6SQ",
    "Accept": "application/json"
  }
)

print(data.content)


