# pcost.py
#
# Exercise 1.27
import sys
import csv


def portfolio_cost(filename):
    cost = 0

    with open(filename, "r") as f:
        data = csv.reader(f)
        next(data)

        for row in data:
            try:
                _, share, price = row
                cost += int(share) * float(price)
            except ValueError:
                print(f"Warning: There is empty columns in {row}")
                continue

    return cost


print("args: ", sys.argv)

filename = "Data/portfolio.csv"
if len(sys.argv) == 2 and sys.argv[1].endswith("csv"):
    filename = sys.argv[1]

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")
