#!/usr/bin/python

import json

def main():

    res = {
        'success': True,
        'changed': True,
        'lolcats': 50000
    }
    print(json.dumps(res))


if __name__ == "__main__":
    main()
