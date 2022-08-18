import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn')

import yfinance as yf

 
# Stock= yf.Ticker('msft')
Stocka=input("Type in your stock ticker here: ")
Stockb=input("Type in your stock ticker here: ")
Stockc=input("Type in your stock ticker here: ")
Stockd=input("Type in your stock ticker here: ")


Stocks = [Stocka,Stockb,Stockc,Stockd]

df =pd.DataFrame()

today=datetime.now().date().strftime('%Y-%m-%d')

for Stock in Stocks:
#The start and end date is adjustable  to ther user terms
    df[Stock] =yf.Ticker(Stock).history(start='2010-01-01', end=today).Close

plt.figure()
plt.plot(df)
plt.ylabel('Price($)')
plt.xlabel('Year')
plt.show()


 