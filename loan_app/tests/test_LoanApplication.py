from loan_app.source.LoanApplication import LoanApplication
from loan_app.source.LoanSummary import LoanSummary


def test_pre_assessment_profit_positive_asset_positive():
    loan_application = LoanApplication("test", "400", "Myob", "2021")
    loan_summary = LoanSummary(loan_application.buisness_name, loan_application.established_year, loan_application.calculateYearlyProfits(), loan_application.loan_amount, loan_application.calculatePreAssessment())
    assert(loan_summary.pre_assessment == 100)


def test_pre_assessment_profit_positive_asset_negative():
    loan_application = LoanApplication("test", "600", "Myob", "2021")
    loan_summary = LoanSummary(loan_application.buisness_name, loan_application.established_year, loan_application.calculateYearlyProfits(), loan_application.loan_amount, loan_application.calculatePreAssessment())
    assert(loan_summary.pre_assessment == 60)


def test_pre_assessment_profit_negative_asset_positive():
    loan_application = LoanApplication("test", "400", "Xero", "2021")
    loan_summary = LoanSummary(loan_application.buisness_name, loan_application.established_year, loan_application.calculateYearlyProfits(), loan_application.loan_amount, loan_application.calculatePreAssessment())
    assert(loan_summary.pre_assessment == 100)


def test_pre_assessment_profit_negative_asset_negative():
    loan_application = LoanApplication("test", "600", "Xero", "2021")
    loan_summary = LoanSummary(loan_application.buisness_name, loan_application.established_year, loan_application.calculateYearlyProfits(), loan_application.loan_amount, loan_application.calculatePreAssessment())
    assert(loan_summary.pre_assessment == 20)


def test_pre_assessment_established_less_than_12_months():
    loan_application = LoanApplication("test", "100", "Myob", "2022")
    loan_summary = LoanSummary(loan_application.buisness_name, loan_application.established_year, loan_application.calculateYearlyProfits(), loan_application.loan_amount, loan_application.calculatePreAssessment())
    assert(loan_summary.pre_assessment == 20)


def test_yearly_profits_list_2022():
    loan_application = LoanApplication("test", "100", "Myob", "2022")
    loan_summary = LoanSummary(loan_application.buisness_name, loan_application.established_year, loan_application.calculateYearlyProfits(), loan_application.loan_amount, loan_application.calculatePreAssessment())
    assert(loan_summary.yearly_profits_list == [{'profit': 900, 'year': 2022}])


def test_yearly_profits_list_2021():
    loan_application = LoanApplication("test", "100", "Myob", "2021")
    loan_summary = LoanSummary(loan_application.buisness_name, loan_application.established_year, loan_application.calculateYearlyProfits(), loan_application.loan_amount, loan_application.calculatePreAssessment())
    assert(loan_summary.yearly_profits_list == [{'profit': 1200, 'year': 2021}, {'profit': 900, 'year': 2022}])

