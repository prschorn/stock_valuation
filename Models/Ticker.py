import json


class Ticker(object):

    def __init__(self, json_data):
        if json_data is not None:
            info = json_data.info
            self.twoHundredDayAverage = info['twoHundredDayAverage']
            self.payoutRatio = info['payoutRatio']
            self.fiftyDayAverage = info['fiftyDayAverage']
            self.trailingAnnualDividendRate = info['trailingAnnualDividendRate']
            self.dividendRate = info['dividendRate']
            self.beta = info['beta']
            self.trailingPE = info['trailingPE']
            self.forwardPE = info['forwardPE']
            self.dividendYield = info['dividendYield']
            self.beta3Year = info['beta3Year']
            self.profitMargins = info['profitMargins']
            self.enterpriseToEbitda = info['enterpriseToEbitda']
            self.revenueQuarterlyGrowth = info['revenueQuarterlyGrowth']
            self.annualReportExpenseRatio = info['annualReportExpenseRatio']
            self.lastFiscalYearEnd = info['lastFiscalYearEnd']
            self.netIncomeToCommon = info['netIncomeToCommon']
            self.trailingEps = info['trailingEps']
            self.threeYearAverageReturn = info['threeYearAverageReturn']
            self.pegRatio = info['pegRatio']
            self.lastCapGain = info['lastCapGain']

    def get_json(self):
        return json.dumps(self.__dict__, sort_keys=True)

    def get_dict(self):
        return self.__dict__
