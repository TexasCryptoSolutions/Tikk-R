# Tikk-R
Simple Python Based Cryptocurrency Ticker(JSON)

JSON
By default the code is pointed towards the bittrex public API. 
"https://api.bittrex.com/api/v1.1/public/getmarketsummary?market="

Example :   user@user:~\$ python3 Tikk-r.py BTC XMR

Refresh Rate
#time.sleep(5.0)
This controls the speed at which Tikk-R does REST API. 

![alt text](http://www.terrorsoundz.com/Preview.png)


  These values are requested via Json API. 
  "Link for more info"
  https://bittrex.github.io/api/v1-1
  
  Update 3-24-2019
  -Simplified command line interface
  -Added color support
  
  
----------Libs Used----------

import time
import sys
import urllib, json
import requests
from termcolor import colored
from urllib.request import urlopen
  
