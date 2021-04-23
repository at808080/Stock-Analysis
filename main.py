import pandas 
import numpy 
import yfinance 
import datetime 
from pandas_datareader import data 
from stock import Stock

yfinance.pdr_override()

####

def getRiskFreeRate():
    return 0.01

####

startdate = datetime.datetime(2019, 1, 1)
presentdate = datetime.datetime.now()
df = data.get_data_yahoo("QQQ", startdate, presentdate)
#print(df.head())
#print(df.columns)

#tsla = yfinance.Ticker("TSLA")

tesla = Stock("Tesla", "TSLA")
cisco = Stock("Cisco", "CSCO")

#print(tesla.getPrices()["Open"][len(tesla.getPrices())-1])
#print(tesla.toString())

#print(tesla.getBalanceSheet().columns[0])
#print(tesla.getPrices())
#print(tesla.getEarnings().head())
#print(tesla.getTicker().get_info())
print(tesla.getEarnings())
print(tesla.getCashFlowStatement())