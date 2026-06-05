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
    
    def exchange_currency(self):
        self.origin.balance #método não funcional, pois ainda não foi implementada a lógica de conversão de moedas.

class Deposit(Transaction):
    
    def __init__(
        self,
        amount: float,
        date: str,
        currency: Currency,
        origin: Account,
        destiny: Account = None):

        super().__init__(amount, currency, date, origin, destiny)

    def execute(self):
        return self.origin.deposit(self.amount)

class Withdrawal(Transaction):
    
    def __init__(
        self,
        amount: float,
        date: str,
        currency: Currency,
        origin: Account,
        destiny: Account = None):

        super().__init__(amount, currency, date, origin, destiny)
    
    def execute(self):
        return self.origin.withdraw(self.amount)

class Transfer(Transaction):
    
    def __init__(
        self,
        amount: float,
        date: str,
        currency: Currency,
        origin: Account,
        destiny: Account):

        super().__init__(amount, currency, date, origin, destiny)
    
    def execute(self):
        self.origin.withdraw(self.amount)
        self.destiny.deposit(self.amount)
        return f"Transfer has successfully been done."

class FxConversion(Transaction): #Método não funcional, pois ainda não foi implementada a lógica de conversão de moedas.
    def __init__(
        self,
        amount: float,
        date: str,
        currency: Currency,
        origin: Account,
        destiny: Account):

        super().__init__(amount, currency, date, origin, destiny)
    
    def exchange_currency(self):
        pass
        