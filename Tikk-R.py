import time
import sys
import urllib, json
import requests
from urllib.request import urlopen

# break filler 
br = '---------------'

#Currsor Position
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

while True:

#json request and conversion
  url = 'https://bittrex.com/api/v1.1/public/getmarketsummaries'
  response = urlopen(url)
  json_obj = json.loads(response.read())
  

  #BTC-XMR
  val = json_obj['result'][198]['Bid']
  mknm = json_obj['result'][198]['MarketName']
  h1 = json_obj['result'][198]['High']
  l1 = json_obj['result'][198]['Low']
  las = json_obj['result'][198]['Last']
  oords = json_obj['result'][198]['OpenBuyOrders']

  #BTC-ETH
  val2 = json_obj['result'][58]['Bid']
  mknm2 = json_obj['result'][58]['MarketName']
  h12 = json_obj['result'][58]['High']
  l12 = json_obj['result'][58]['Low']
  las2 = json_obj['result'][58]['Last']
  oords2 = json_obj['result'][58]['OpenBuyOrders']

#convert Data to strings
  obo = str(oords)
  obo2 = str(oords2)
  l = str(l1)
  h = str(h1)
  x = str(val)

  l2 = str(l12)
  h2 = str(h12)
  x2 = str(val2)
#set print format for decimals EX. 0.0000564
  lst = format(las , '.8f')
  g = format(val  , '.8f')
  lst2 = format(las2 , '.9f')
  g2 = format(val2  , '.9f')
# print time in 24HR
  timestamp = time.strftime('%H:%M:%S')

  print(mknm,": " +g,"High: " +h,"Low: " +l,"Last: " +lst,"Time: " +timestamp,"Open BUY Orders: " +obo, end = "\n")    
  print(mknm2,": " +g2,"High: " +h2,"Low: " +l2,"Last: " +lst2,"Time: " +timestamp,"Open BUY Orders: " +obo2, end = "\r")

#clear Terminal 
  sys.stdout.flush()
  sys.stdout.write(CURSOR_UP_ONE)
  sys.stdout.write(ERASE_LINE)
#Loop Reload Time
  time.sleep(5.0)

