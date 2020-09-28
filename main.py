import json
from services import file_services as fs, stocks_services as st

data = []
tickers_data = []

with open('tickers.json') as json_file:
    data = json.load(json_file)

for group in data:
    for industry in group:
        group_tickers = []
        for ticker in group[industry]:
            ticker_info = st.get_ticker_data(ticker)

            if ticker_info is not None:
                group_tickers.append({ticker: ticker_info})

        tickers_data.append({industry: group_tickers})
fs.save_json(tickers_data, 'data.json')
fs.generate_xlsx(tickers_data, 'data.xlsx')

