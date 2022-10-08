from abc import ABC, abstractmethod

class AccountingSystemIntegration(ABC):
    # This abstract class is meant to act like an interface for different Acounting System Integrations
    # All new Accounting System Integrations must extend this class

    @abstractmethod
    def getBalanceSheet(self):
        pass
