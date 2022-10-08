from dataclasses import dataclass

@dataclass
class LoanSummary:
    buisness_name: str
    established_year: int
    yearly_profits_list: list
    loan_amount: int
    pre_assessment: int


    def sendSummaryToDecisionEngine(self):
        return True # Mocking desicion engine request was successful
