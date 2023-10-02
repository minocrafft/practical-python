# pcost.py
#
# Exercise 1.27
import sys
from report import read_portfolio


def portfolio_cost(filename: str) -> float:
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = read_portfolio(filename)
    return sum([s.cost for s in portfolio])


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f"Usage: {argv[0]} portfoliofile")

    _, _portfolio = argv
    cost = portfolio_cost(_portfolio)
    print(f"Total cost: {cost}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
