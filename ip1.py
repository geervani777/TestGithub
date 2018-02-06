import requests
url = "https://api.ipify.org"
respones = requests.get('https://api.ipify.org').text
print('My public IP address is: {}'.format(respones))
