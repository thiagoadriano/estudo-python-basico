import requests

req = requests.get('https://google.com')
print(req.text)
print(req.url)
print(req.cookies['NID'])