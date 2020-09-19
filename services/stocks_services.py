import string

import yfinance as yf


def get_ticker_data(tickers: string):
    ticker_data = yf.Ticker(tickers)
    data = {}
    try:
        data = ticker_data.info
    except:
        data = {}

    return data
