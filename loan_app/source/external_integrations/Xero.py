from .AccountingSoftwareIntegration import AccountingSystemIntegration
from datetime import datetime


class Xero(AccountingSystemIntegration):
    def __init__(self):
        pass


    def getBalanceSheet(self, established_year):
        return self.mockBalanceSheet(established_year)

    
    def mockBalanceSheet(self, established_year):
        balance_sheet = []
        current_date = datetime.now().date()
        if established_year > current_date.year:
            raise Exception(f"{established_year} is invalid")
        
        for year in range(established_year,current_date.year):
            for month in range(1,13):
                balance_sheet.append({"month": month, "year": year,"profit": -100,"asset_value": 500})

        for month in range(1,current_date.month):
                balance_sheet.append({"month": month, "year": current_date.year,"profit": -100,"asset_value": 500})
        return balance_sheet
    