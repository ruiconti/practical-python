class Stock:
    __slots__ = ("name", "_shares", "price")
    
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self.price = price

    def __repr__(self):
        return f"<Stock {self.name}>"

    def __getitem__(self, item):
        return self.__dict__[item]

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    @property
    def shares(self):
        return self._shares
        
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected an int")
        self._shares = value
