from collections import Counter
from stock import Stock
from fileparse import parse_csv


class Portfolio:
    def __init__(self):
        self._holdings = []

    def append(self, holding):
        if not isinstance(holding, Stock):
            raise TypeError("Expected a Stock instance")
        self._holdings.append(holding)

    @classmethod
    def from_csv(cls, lines, **kwargs):
        self = cls()
        portfolio = parse_csv(
            lines,
            select=["name", "shares", "price"],
            types=[str, int, float],
            **kwargs,
        )

        for d in portfolio:
            self.append(Stock(**d))

        return self

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

    @property
    def cost(self):
        return sum(s.shares * s.price for s in self._holdings)

    def tabulate_shares(self):
        shares = Counter()
        for s in self._holdings:
            shares[s.name] += s.shares

        return shares
