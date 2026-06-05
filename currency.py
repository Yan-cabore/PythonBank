from abc import ABC, abstractmethod
class Currency(ABC):
    def __init__(
            self,
            code: str,
            symbol: str,
            exchange_rate: float):
        
        self.code = code
        self.symbol = symbol
        self.exchange_rate = exchange_rate
    
class BRL(Currency):
    def __init__(self):
        super().__init__("BRL", "R$", 1.0)
class USD(Currency):
    def __init__(self):
        super().__init__("USD", "$", 0.20)
class EUR(Currency):
    def __init__(self):
        super().__init__("EUR", "€", 0.18)
    
