from abc import ABC, abstractmethod
from PythonBank.account import Account
from currency import Currency

class Transaction(ABC):
    def __init__(
        self,
        amount: float,
        currency: Currency,
        date: str,
        origin: Account = None,
        destiny: Account = None):
        
        self.destiny = destiny
        self.origin = origin
        self.amount = amount
        self.currency = currency
        self.date = date
    @abstractmethod
    def execute(self):
        pass 
    
    def convert_currency(self, currency: Currency):
        exchanged_currency = self.amount * currency.exchange_rate
        return exchanged_currency