from .typedproperty import String, Integer, Float


class Stock:
    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares: int):
        self.shares -= shares

    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"
