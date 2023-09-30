# report.py
#
# Exercise 2.4
from fileparse import parse_csv


def read_portfolio(filename: str) -> list[dict]:
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    return parse_csv(
        filename,
        select=["name", "shares", "price"],
        types=[str, int, float],
    )


def read_prices(filename: str) -> dict:
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    return dict(parse_csv(filename, types=[str, float], has_headers=False))


def make_report(portfolio: list[dict], prices: dict) -> list[tuple]:
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    reports = []

    for stock in portfolio:
        curr_price = prices[stock["name"]]
        change = curr_price - float(stock["price"])
        reports.append((stock["name"], stock["shares"], curr_price, change))

    return reports


def print_report(report: list[tuple]):
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % headers)
    print("{:->10s} {:->10s} {:->10s} {:->10s}".format("", "", "", ""))

    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")


def portfolio_report(portfolio: str, prices: str):
    _portfolio = read_portfolio(portfolio)
    _prices = read_prices(prices)
    _report = make_report(_portfolio, _prices)
    print_report(_report)


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f"Usage: {argv[0]} portfoliofile pricefile")

    _, _portfolio, _prices = argv
    portfolio_report(_portfolio, _prices)


if __name__ == "__main__":
    import sys

    main(sys.argv)
