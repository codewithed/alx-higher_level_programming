#!/usr/bin/python3
'''
Send an email to a URL using a POST request and display the response body
'''

import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: ', __file__, 'URL', 'email', file=sys.stderr)
        sys.exit(1)

    DATA = urlencode({'email': sys.argv[2]}).encode()
    try:
        with urlopen(sys.argv[1], DATA) as r:
            print(r.read().decode())
    except HTTPError as exc:
        print('Error code:', exc.code)
        sys.exit(1)
    except URLError as exc:
        print('Error:', exc.reason)
        sys.exit(1)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
