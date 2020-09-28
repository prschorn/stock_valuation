import string

import yfinance as yf

from Models.Ticker import Ticker


def get_ticker_data(tickers: string):
    ticker_data = yf.Ticker(tickers)
    try:
        ticker_info = Ticker(ticker_data)
        data = ticker_info.get_dict()
    except Exception:
        data = None

    return data
