# report.py
#
# Exercise 2.4
import logging
from .formatter import create_formatter
from .fileparse import parse_csv
from .stock import Stock
from .portfolio import Portfolio


logging.basicConfig(filename="app.log", filemode="w", level=logging.DEBUG)


def read_portfolio(filename: str, **kwargs):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **kwargs)


def read_prices(filename: str, **kwargs) -> dict:
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False, **kwargs))


def make_report(portfolio, prices: dict) -> list[tuple]:
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    reports = []
    for stock in portfolio:
        curr_price = prices[stock.name]
        change = curr_price - stock.price
        reports.append((stock, curr_price, change))

    return reports


def print_report(report: list[tuple], formatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(("Name", "Shares", "Price", "Change"))
    for stock, price, change in report:
        row = [stock.name, str(stock.shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(row)


def portfolio_report(portfolio: str, prices: str, fmt: str = "txt"):
    _portfolio = read_portfolio(portfolio)
    _prices = read_prices(prices)
    _report = make_report(_portfolio, _prices)
    formatter = create_formatter(fmt)
    print_report(_report, formatter)


def main(argv):
    if len(argv) < 3:
        raise SystemExit(
            f"Usage: {argv[0]} portfoliofile pricefile (option: tableformat)"
        )

    if len(argv) == 3:
        _, _portfolio, _prices = argv
        portfolio_report(_portfolio, _prices)
    elif len(argv) == 4:
        _, _portfolio, _prices, fmt = argv
        portfolio_report(_portfolio, _prices, fmt)


if __name__ == "__main__":
    import sys

    main(sys.argv)
