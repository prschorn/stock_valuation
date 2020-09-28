# stock_valuation
This project has the intent to compile stocks data to help analyzing and taking better decisions on investments


# V0.1
Downloads ticker informations based on the file tickers.json and write them on the file data.json grouping by industry and ticker.


# Next steps

     - Normalize data on a spreadsheet after downloading
     - Add calculations on the data. eg Peg Ratio, CAGR, Beta, P/E, Div Yield etc.
     - Start recommendation system based on analysis over calculations and set priorities on the spreadsheet.
     
# Project setup

    - Create virtual env (Python 3) python3 -m venv env
    - Activate venv: source env/bin/activate
    - pip install yfinance
    - pip install lxml
    - pip install xlsxwriter
    
