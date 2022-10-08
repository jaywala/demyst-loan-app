from .external_integrations.Myob import Myob
from .external_integrations.Xero import Xero

class LoanApplication:
    def __init__(self, buisness_name, loan_amount, asp, established_year) -> None:
        self.buisness_name = buisness_name
        self.loan_amount = int(loan_amount)
        self.asp = asp # Accounting Software Provider
        self.established_year = int(established_year)
        self.balance_sheet = self.getBalanceSheet()

    def getBalanceSheet(self):
        if self.asp == "Myob":
            asp = Myob()
        elif self.asp == "Xero":
            asp = Xero()
        return  asp.getBalanceSheet(self.established_year)
    

    def calculatePreAssessment(self):
        if len(self.balance_sheet) >= 12:
            last_12_months = self.balance_sheet[-12:]
            if sum((x['asset_value'] for x in last_12_months)) /12 > self.loan_amount:
                return 100
            elif sum((x['profit'] for x in last_12_months)) > 0:
                return 60
        return 20


    def calculateYearlyProfits(self):
        yearly_profits = []
        year = self.established_year
        profit = 0

        for balance in self.balance_sheet:
            if year != balance['year']:
                yearly_profits.append({"year": year, "profit": profit})
                year = balance['year']
                profit = 0
            profit += balance['profit']
        
        yearly_profits.append({"year": year, "profit": profit})
        return yearly_profits
