class Investment:
    def __init__(self, name: str, amount: float, return_rate: float, date: int):
        
        self.name = name
        self.amount = amount
        self.return_rate = return_rate
        self.date = date
    
class Portfolio:
    def __init__(self):
        self._investments = []
    
    def add_investment(self, investment: Investment):
        self._investments.append(investment)
    
    def summary(self):
        for investment in self._investments:
            print(self._investments[investment]) # vai ficar para o futuro a correção diss aqui
        
    def delete(self, name):
        for investment in self._investments:
            if investment.name == name:
                self._investments.remove(investment)
                break
        

