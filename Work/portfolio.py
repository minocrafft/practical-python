from collections import Counter


class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings

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
