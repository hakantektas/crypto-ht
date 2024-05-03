import requests
import json
from datetime import datetime

# Get current date and time
simdi = datetime.now()
def get_rsi(symbol):
    # Binance API endpoint
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=4h&limit=14"

    # Get data from Binance API
    response = requests.get(url)
    data = response.json()

    # Get closing prices
    closes = [float(entry[4]) for entry in data]

    # RSI calculation
    ups = sum([closes[i + 1] - closes[i] for i in range(13) if closes[i + 1] > closes[i]])
    downs = sum([-1 * (closes[i + 1] - closes[i]) for i in range(13) if closes[i + 1] < closes[i]])

    avg_gain = ups / 14
    avg_loss = downs / 14

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi

def get_usdt_symbols():
    # Binance API endpoint
    url = "https://api.binance.com/api/v3/exchangeInfo"

    # Get symbols from the Binance API
    response = requests.get(url)
    data = response.json()

    # Filter symbols with USDT parity .
    usdt_symbols = [symbol['symbol'] for symbol in data['symbols'] if symbol['quoteAsset'] == 'USDT']

    return usdt_symbols

if __name__ == "__main__":
    # Buy symbols with the USDT pair
    usdt_symbols = get_usdt_symbols()
    # Print date and time information in any format
    print("Current date and time:", simdi)
    # List coins with RSI below 29
    print("Coins with RSI below 29:")
    for symbol in usdt_symbols:
        rsi = get_rsi(symbol)
        if rsi < 29:
            print(f"{symbol}: RSI={rsi}")
