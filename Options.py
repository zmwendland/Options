# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:54:55 2022

@author: Zach
"""

from optionprice import Option as op
from datetime import datetime as dt
import pandas as pd
import numpy as np
import pandas_datareader as web
from yahoofinancials import YahooFinancials as yho


stock = ['OXY'] #<--- ENTER TICKER
yf = yho(stock)
curr_prices = yf.get_current_price()

my_dict = curr_prices
my_list = list(my_dict.values())
current_price = my_list[0]

start = datetime(2022,1,1)

price = []
 
for s in stock:
    r = web.DataReader(s,'yahoo',start)
    r['stock'] = s
    price.append(r)
    
df = pd.concat(price)  
df = df.reset_index()
df = df[['Date','stock','Close']]

mean = np.mean(df['Close'])

dev = []

for p in df['Close']:
    devs = p - mean
    dev.append(devs)

sqrt = np.square([x for x in dev])
sum_sqrt = np.sum([x for x in sqrt])
var = sum_sqrt/df['Close'].count()
vol_stdev = np.sqrt(var)

#OPTION = manipulate s0, start, and maybe sigma to see price in future
some_opt = op(european=False,
                  kind = 'call',#<--- CHOOSE CALL OR PUT (lowercase)
                  s0=current_price,
                  k=65, #<--- ENTER STRIKE PRICE
                  sigma = .5546, #<--- VOL INDEX/IV
                  r = .02757, #<--- 10 YEAR T-BILL RATE
                  start = dt(2022,8,9),
                  end = dt(2022,8,19),
                  dv=0)
price2 = some_opt.getPrice()
print(price2)


