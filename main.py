import json
import stocks as st
import file_services as fs

data = []
tickers_data = []

with open('tickers.json') as json_file:
    data = json.load(json_file)

for group in data:
    for industry in group:
        group_tickers = []
        for ticker in group[industry]:
            ticker_data = {
                ticker: st.get_ticker_data(ticker)
            }
            group_tickers.append(ticker_data)
        industry_data = {
            industry: group_tickers
        }
        tickers_data.append(industry_data)

fs.save_json(tickers_data, 'data.json')

