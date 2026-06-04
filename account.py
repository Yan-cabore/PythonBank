from currency import Currency
from abc import ABC, abstractmethod
 
class Account(ABC):
    def __init__(self, account_id: int, holder: str, balance: float, currency: Currency):
        
        self.account_id = account_id
        self.holder = holder
        self.balance = balance
        self.currency = currency
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def check_balance(self):
        pass #possivelmente concatenar aqui o code

class CheckingAccount(Account):
    def __init__(self, account_id, holder, balance, currency):
        super().__init__(account_id, holder, balance, currency)
    
    def deposit(self, amount):
        pass
    
    def withdraw(self, amount):
        pass
    
    def check_balance(self):
        pass
