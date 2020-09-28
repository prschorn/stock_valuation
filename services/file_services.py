import string
import json
import xlsxwriter


def save_json(data, filename: string):
    file = open(f"output/{filename}", 'w')
    file.write(json.dumps(data, indent=4, sort_keys=True))


def generate_xlsx(data, filename: string):
    try:
        workbook = xlsxwriter.Workbook(f"output/{filename}")

        for industry in data:
            for industry_name in industry:
                worksheet = workbook.add_worksheet(industry_name)
                add_header(worksheet)
                add_tickers_data(worksheet, industry)

        workbook.close()
    except Exception as e:
        error = e


def add_tickers_data(sheet, industries):
    line_number = 2
    for industry_type in industries:
        for tickers in industries[industry_type]:
            for ticker in tickers:
                ticker_data = tickers[ticker]
                sheet.write(f'A{line_number}', ticker)
                sheet.write(f'B{line_number}', ticker_data['annualReportExpenseRatio'])
                sheet.write(f'C{line_number}', ticker_data['beta'])
                sheet.write(f'D{line_number}', ticker_data['beta3Year'])
                sheet.write(f'E{line_number}', ticker_data['dividendRate'])
                sheet.write(f'F{line_number}', ticker_data['dividendYield'])
                sheet.write(f'G{line_number}', ticker_data['enterpriseToEbitda'])
                sheet.write(f'H{line_number}', ticker_data['fiftyDayAverage'])
                sheet.write(f'I{line_number}', ticker_data['forwardPE'])
                sheet.write(f'J{line_number}', ticker_data['lastCapGain'])
                sheet.write(f'K{line_number}', ticker_data['lastFiscalYearEnd'])
                sheet.write(f'L{line_number}', ticker_data['netIncomeToCommon'])
                sheet.write(f'M{line_number}', ticker_data['payoutRatio'])
                sheet.write(f'N{line_number}', ticker_data['pegRatio'])
                sheet.write(f'O{line_number}', ticker_data['profitMargins'])
                sheet.write(f'P{line_number}', ticker_data['revenueQuarterlyGrowth'])
                sheet.write(f'Q{line_number}', ticker_data['threeYearAverageReturn'])
                sheet.write(f'R{line_number}', ticker_data['trailingAnnualDividendRate'])
                sheet.write(f'S{line_number}', ticker_data['trailingEps'])
                sheet.write(f'T{line_number}', ticker_data['trailingPE'])
                sheet.write(f'U{line_number}', ticker_data['twoHundredDayAverage'])
                line_number += 1


def add_header(sheet):
    sheet.write('A1', 'Ticker')
    sheet.write('B1', 'annualReportExpenseRatio')
    sheet.write('C1', 'beta')
    sheet.write('D1', 'beta3Year')
    sheet.write('E1', 'dividendRate')
    sheet.write('F1', 'dividendYield')
    sheet.write('G1', 'enterpriseToEbitda')
    sheet.write('H1', 'fiftyDayAverage')
    sheet.write('I1', 'forwardPE')
    sheet.write('J1', 'lastCapGain')
    sheet.write('K1', 'lastFiscalYearEnd')
    sheet.write('L1', 'netIncomeToCommon')
    sheet.write('M1', 'payoutRatio')
    sheet.write('N1', 'pegRatio')
    sheet.write('O1', 'profitMargins')
    sheet.write('P1', 'revenueQuarterlyGrowth')
    sheet.write('Q1', 'threeYearAverageReturn')
    sheet.write('R1', 'trailingAnnualDividendRate')
    sheet.write('S1', 'trailingEps')
    sheet.write('T1', 'trailingPE')
    sheet.write('U1', 'twoHundredDayAverage')
