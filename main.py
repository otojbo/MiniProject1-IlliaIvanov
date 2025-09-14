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