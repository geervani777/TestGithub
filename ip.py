import requests
url = "https://api.db-ip.com/addrinfo?api_key=1172cb13a4559bd12b00f80fe960005ba3dbf1aa&addr=139.59.2.223"
respones = requests.get(url)
data = respones.content
print(data)
