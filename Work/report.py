# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    portfolio = []

    with open(filename, "r") as f:
        rows = csv.reader(f)
        next(rows)

        for row in rows:
            name, shares, price = row
            portfolio.append(
                {
                    "name": name,
                    "shares": int(shares),
                    "price": float(price),
                }
            )

    return portfolio


def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    prices = {}

    with open(filename, "r") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name, price = row
                prices[name] = float(price)
            except ValueError:
                pass

    return prices


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

# Calculate the total property of the portfolio
property = 0
for stock in portfolio:
    try:
        property += (stock["price"] - prices[stock["name"]]) * stock["shares"]
    except KeyError:
        print(f"Warning: prices has no {stock['name']}")
        continue

print(f"Property: {property}")
