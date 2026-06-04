from abc import ABC, abstractmethod
from currency import Currency

class Transaction(ABC):
    def __init__(self, transaction_id: int, amount: float, currency: Currency, date: str):
        
        self.transaction_id = transaction_id
        self.amount = amount
        self.currency = currency
        self.date = date
    
    @abstractmethod
    def execute(self):
        pass

    def convert_currency(self):
        pass