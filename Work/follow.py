import os
import time
import report

PATH_PORTFOLIO = "Data/portfolio.csv"
PATH_STOCK_DATA = "Data/stocklog.csv"


def follow(filepath):
    f = open(filepath)
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if line == "":
            time.sleep(0.1)
            continue
        yield line


if __name__ == "__main__":
    portfolio = report.read_portfolio(PATH_PORTFOLIO)
    for line in follow(PATH_STOCK_DATA):
        fields = line.split(",")
        name = fields[0].strip('"')
        price = float(fields[1])
        if name in portfolio:
        change = float(fields[4])
            print(f"{name:>10s} {price:>10.2f} {change:>10.4f}")
