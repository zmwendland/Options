from optionprice import Option as op
from datetime import datetime as dt
import pandas as pd
from datetime import datetime, timezone, timedelta
from yahoo_fin import stock_info as si
import pandas_datareader as web
from yahoofinancials import YahooFinancials as yho
from time import sleep

""" Inputs """
strike = 72.5       #<----- ENTER STRIKE  
stock = 'uso'       #<--- ENTER TICKER
opt_type = 'call'   #<--- ENTER 'call' or 'put'
pp = .37            #<------- ENTER PURCHASE PRICE PER CONTRACT
contracts1 = 1      #<--- ENTER NUMBER OF CONTRACTS
expiry_date = dt(2022,9,2)   #<------ ENTER EXPIRATION DATE
volatility = .9018  #<--- ENTER VOL INDEX/IV OF EXPIRY
""" """

yf = yho(stock)

if si.get_market_status() == 'REGULAR':
    curr_prices22 = si.get_live_price(stock)

elif si.get_market_status != 'REGULAR':
    curr_prices22 = si.get_premarket_price(stock)

purchases = pp*100
start = datetime(2022,1,1)
timezone_offset = -10.0
tzinfo = timezone(timedelta(hours=timezone_offset))
    
price = []
    
for s in stock:
    r = web.DataReader(s,'yahoo',start)
    r['stock'] = s
    price.append(r)

rfr = ['^TNX']
yf2 = yho(rfr)
curr_rfr = yf2.get_current_price()

my_dict2 = curr_rfr
my_list2 = list(my_dict2.values())
current_rfr= my_list2[0]/100

some_opt = op(european=False,
                    kind = opt_type,
                    s0 = curr_prices22,
                    k = strike,
                    sigma = volatility, 
                    r = current_rfr, #<--- 10 YEAR T-BILL RATE
                    start = dt.now(tzinfo),
                    end = expiry_date,
                    dv=0)

price21 = some_opt.getPrice(method='BSM',iteration=5000000)*100
gain = round(price21-purchases,2)*contracts1
while True:
    print('')
    print('Stock Ticker: ', stock.upper())
    print('')
    print('Time: ', si.get_market_status()," MARKET HOURS")
    print('')
    print('Current Stock Price:',"${:.2f}".format(curr_prices22))
    sleep(2)
    print('')
    print('Current Option Price:',"${:.2f}".format(round(price21,2)))
    print('')
    sleep(2)
    print('Gain/Loss:',"${:.2f}".format(round(gain,2)))
    print('')
    sleep(2)
    print('% G/L: ','{:.1%}'.format(price21/purchases-1))
    print('')
    sleep(2)
    print('---------------------------------------')
    sleep(2)
    if si.get_market_status != 'REGULAR':
        break
    else:
        sleep(10)
        continue
    
    
        
        
        
    
    

        


