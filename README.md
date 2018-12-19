# Tikk-R
Simple Python Based Cryptocurrency Ticker(JSON)

JSON
By default the code is pointed towards the bittrex public API. 

Example :   url = 'https://bittrex.com/api/v1.1/public/getmarketsummaries'

Refresh Rate
#time.sleep(5.0)
This controls the speed at which Tikk-R does JSON API Request. 

![alt text](http://www.terrorsoundz.com/Preview.png)




Ticker Symbol Definitions 
  #BTC-XMR
  val = json_obj['result'][198]['Bid']
  mknm = json_obj['result'][198]['MarketName']
  h1 = json_obj['result'][198]['High']
  l1 = json_obj['result'][198]['Low']
  las = json_obj['result'][198]['Last']
  oords = json_obj['result'][198]['OpenBuyOrders']
  
  These values are requested via Json API. 
  "Link for more info"
  https://bittrex.zendesk.com/hc/en-us/articles/115003723911-Developer-s-Guide-API
  
  
  
