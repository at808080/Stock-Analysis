import pandas 
import numpy 
import yfinance 
import datetime 
from pandas_datareader import data 

class Stock:
    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker

    def getPrices(self):
        return data.get_data_yahoo(self.ticker)

    def getTicker(self):
        return yfinance.Ticker(self.ticker)

    def getFinancials(self):
        return self.getTicker().financials

    def getBalanceSheet(self):
        return self.getTicker().balance_sheet

    def getEarnings(self):
        return self.getTicker().earnings

    def getDividends(self):
        return self.getTicker().dividends

    def getCashFlowStatement(self):
        return self.getTicker().cashflow


    def toString(self):
        print("This stock is " + self.name + " with ticker " + self.ticker + " and is currently at " + str(self.getPrices()["Open"][len(self.getPrices()["Open"])-1]))



"""
https://pypi.org/project/yfinance/
If you want to use a proxy server for downloading data, use:

import yfinance as yf

msft = yf.Ticker("MSFT")

msft.history(..., proxy="PROXY_SERVER")
msft.get_actions(proxy="PROXY_SERVER")
msft.get_dividends(proxy="PROXY_SERVER")
msft.get_splits(proxy="PROXY_SERVER")
msft.get_balance_sheet(proxy="PROXY_SERVER")
msft.get_cashflow(proxy="PROXY_SERVER")
msft.option_chain(..., proxy="PROXY_SERVER")
"""