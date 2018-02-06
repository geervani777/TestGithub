import json
import requests
ip_address = input("enter the ip address:")
auth = 'c65fa52a-b87b-406c-87f5-37968ff95d60';
url = 'https://ipfind.co/?auth=' + auth + '&ip=' + ip_address;
#response = urlopen(url)(some times we using the urlopen we can't split the data. so that the resion only we can modifing the code)
#data = json.loads(response.read())
response = requests.get(url)
data = response.text
#print(data)
bpi = data.split(':')
bpi1 = bpi[2]
bpi2 = bpi1.split(',')
bpi3 = bpi2[0]
print(bpi3)
