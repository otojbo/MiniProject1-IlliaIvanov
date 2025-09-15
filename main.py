# INF 601 - Advanced Python
# Illia Ivanov
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pathlib import Path

STOCKS = ["AAPL","MSFT","GOOGL","AMZN","TSLA"]

charts_dir = Path("charts")
charts_dir.mkdir(exist_ok=True)

def get_last_10_closes(stock: str) -> np.ndarray:
    history = yf.Ticker(stock).history(period="20d", interval="1d")
    closes = history["Close"].dropna().tail(10).tolist()
    return np.array(closes, dtype=float)

def save_chart(stock: str, prices: np.ndarray):
    days = range(1, len(prices) + 1)

    plt.figure()
    plt.plot(days, prices, marker="o")
    plt.title(stock)
    plt.xlabel("Trading Days")
    plt.ylabel("Closing Price")
    plt.tight_layout()
    plt.savefig(charts_dir / f"{stock}.png")
    plt.close()

def main():
    for stock in STOCKS:
        prices = get_last_10_closes(stock)
        if prices.size == 10:
            save_chart(stock, prices)

if __name__ == "__main__":
    main()