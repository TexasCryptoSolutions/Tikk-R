import time
import sys
import urllib, json
import requests
from termcolor import colored
from urllib.request import urlopen

# break filler 
br = '---------------'

#Currsor Position
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
coin = str(sys.argv[1])
coin1 = str(sys.argv[2])

if len(sys.argv) == 1:
  print("Please input two 3 Letter coin names EX: python3 tickk-r.py BTC XMR ")
  quit()

value = str(coin) + str(coin1)

while True:

#json request and conversion
  url = 'https://api.bittrex.com/api/v1.1/public/getmarketsummary?market=' + coin + '-' + coin1
  response = urlopen(url)
  json_obj = json.loads(response.read())

  	
  #BTC-XMR
  val = json_obj['result'][0]['Bid']
  mknm = colored(json_obj['result'][0]['MarketName'], 'yellow')
  h1 = colored(json_obj['result'][0]['High'], 'green')
  l1 = colored(json_obj['result'][0]['Low'], 'red')
  las = json_obj['result'][0]['Last']
  oords = colored(json_obj['result'][0]['OpenBuyOrders'], 'magenta')


#convert Data to strings
  obo = str(oords)
  obo2 = str(oords)
  l = str(l1)
  h = str(h1)
  x = str(val)

  l2 = str(l1)
  h2 = str(h1)
  x2 = str(val)


#set print format for decimals EX. 0.0000564
  lst = colored(format(las , '.8f'), 'blue')
  g = format(val  , '.8f')
  lst2 = format(las , '.9f')
  g2 = format(val  , '.9f')
#     print time in 24HR
  timestamp = colored(time.strftime('%H:%M:%S'), 'red')

  print(mknm,": " +g,"High: " +h,"Low: " +l,"Last: " +lst,"Time: " +timestamp,"Open BUY Orders: " +obo, end = "\n")    


#clear Terminal 
  sys.stdout.flush()
  sys.stdout.write(CURSOR_UP_ONE)
  sys.stdout.write(ERASE_LINE)
#Loop Reload Time
time.sleep(0.1)
