#!/usr/bin/python3
'''
Take a letter and send a POST request to http://0.0.0.0:5000/search_user
'''

import sys
import requests

URL = 'http://0.0.0.0:5000/search_user'

if __name__ == '__main__':

    data = {'q': '' if len(sys.argv) == 1 else sys.argv[1]}
    resp = requests.post(URL, data=data)
    try:
        json = resp.json()
    except JSONDecodeError:
        print('Not a valid JSON')
    else:
        if json:
            print('[{}] {}'.format(json['id'], json['name']))
        else:
            print('No result')
