#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""OSINT - This is a simple Python script to search mac vendor info"""

__author__      = "Adriano Freitas"
__copyright__   = "Copyright 2022, Night City"
__license__ = "GPL"
__version__ = "3.0"

import os
import commands
import requests
from argparse import ArgumentParser
from requests.exceptions import HTTPError

class color:
    FAIL = '\033[91m'
    BLUE = '\033[94m'
    BLUE2 = '\033[1;36m'
    INFO = '\033[93m'
    ENDC = '\033[0m'
    GREEN = '\033[1;32m'

VERSION = "1.0"
SAMPLES = """
$ python3 macvendor --help
usage: python3 macvendor --search MAC-ADDRESS

OSINT - This is a simple Python script to search payment of civil servant.

options:
  -h, --help            show this help message and exit
  -v, --version         Version
  -s MAC, --search MAC     Mac Address to Search to search
"""

def search(mac_address):    
    url = "https://api.macvendors.com/"    
    link = url + mac_address
    try:
        r = requests.get(link)
        print("\n [d] " + color.BLUE + "Search: " + color.ENDC + mac_address)                             

        # If the response was successful, no Exception will be raised
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print("\n [d] " + color.GREEN + "Found: " + color.ENDC + mac_address[:6])
        print("Vendor: {}".format(r.text))
        
                  
def main():  
    # Get arguments
    argp = ArgumentParser()
    argp = ArgumentParser(description="This is a simple Python script to search mac vendor info", usage="python macvendor --search <MAC-ADDRESS>")    
    argp.add_argument('-v', '--version', dest='version', action="store_true", help='Version')    
    argp.add_argument('-s', '--search', dest='mac_address', required=False, help='MAC Address to search')
    
    args = argp.parse_args()    
    
    if args.version:
        print(SAMPLES)
    elif args.mac_address:        
        print("\n [i] " + color.INFO + "Checking..." + color.ENDC)
        search(args.mac_address)
    else:        
        print(SAMPLES)                                
        print("\n")
        

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()