from currency import Currency
from portfolio import Investment, Portfolio
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(
        self,
        account_id: int,
        holder: str,
        balance: float,
        currency: Currency
    ):
        self.account_id = account_id
        self.holder = holder
        self.balance = balance
        self.currency = currency

    @abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_balance(self):
        return f"{self.balance}{self.currency.code}"


class CheckingAccount(Account):
    def __init__(
        self,
        account_id,
        holder,
        balance,
        currency,
        overdraft_limit: float = -1000
    ):
        super().__init__(account_id, holder, balance, currency)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if (self.balance - amount) < self.overdraft_limit:
            return "Error: withdraw limit reached."

        self.balance -= amount
        return f"You withdrew {amount}\nCurrent balance: {self.balance}"


class SavingsAccount(Account):
    def __init__(
        self,
        account_id,
        holder,
        balance,
        currency,
        interest_rate: float
    ):
        super().__init__(account_id, holder, balance, currency)
        self._interest_rate = interest_rate

    def update_balance(self):
        self.balance *= (1 + self._interest_rate)
        return f"Your current savings {self.balance}"

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            return "Your balance is currently zero"

        self.balance -= amount
        return f"You withdrew {amount}\nCurrent balance: {self.balance}"


class InvestmentAccount(Account):
    def __init__(self, account_id, holder, balance, currency):
        super().__init__(account_id, holder, balance, currency)
        self._portfolio = Portfolio()

    def invest(self, name, amount, return_rate, date):
        if self.balance - amount < 0:
            return "Error: not enough balance."

        self.balance -= amount
        self._portfolio.add_investment(
            Investment(name, amount, return_rate, date)
        )

        return "Your investment has been successfull."

    def withdraw(self, amount):
        if self.balance - amount < 0:
            return "Error: not enough balance."

        self.balance -= amount
        return "Your investment has been successfull."