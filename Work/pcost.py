# pcost.py
#
# Exercise 1.27
import sys
from report import read_portfolio


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = read_portfolio(filename)

    cost = sum([stock["shares"] * stock["price"] for stock in portfolio])
    return cost


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f"Usage: {argv[0]} portfoliofile")

    _, _portfolio = argv
    cost = portfolio_cost(_portfolio)
    print(f"Total cost: {cost}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
