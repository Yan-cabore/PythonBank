from abc import ABC, abstractmethod
class Currency(ABC):
    def __init__(self, code: str, symbol: str, exchange_rate: float):
        
        self.code = code
        self.symbol = symbol
        self.exchange_rate = exchange_rate
    
    
    
