import requests
import re

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = f'http://{username}.natas.labs.overthewire.org'

data = { 'secret' : 'oubWYf2kBq', 'submit' : 'hi' }

response = requests.post(url, data = data, auth = (username, password))
content = response.text

print(re.findall('The password for natas9 is (.*)', content)[0])