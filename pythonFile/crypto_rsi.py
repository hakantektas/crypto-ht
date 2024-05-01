import requests
import json
from datetime import datetime

# Şu anki tarih ve saat bilgisini al
simdi = datetime.now()
def get_rsi(symbol):
    # Binance API endpoint'i
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1h&limit=14"

    # Binance API'sinden veri al
    response = requests.get(url)
    data = response.json()

    # Kapanış fiyatlarını al
    closes = [float(entry[4]) for entry in data]

    # RSI hesaplama
    ups = sum([closes[i + 1] - closes[i] for i in range(13) if closes[i + 1] > closes[i]])
    downs = sum([-1 * (closes[i + 1] - closes[i]) for i in range(13) if closes[i + 1] < closes[i]])

    avg_gain = ups / 14
    avg_loss = downs / 14

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi

def get_usdt_symbols():
    # Binance API endpoint'i
    url = "https://api.binance.com/api/v3/exchangeInfo"

    # Binance API'sinden sembolleri al
    response = requests.get(url)
    data = response.json()

    # USDT paritesine sahip sembolleri filtrele
    usdt_symbols = [symbol['symbol'] for symbol in data['symbols'] if symbol['quoteAsset'] == 'USDT']

    return usdt_symbols

if __name__ == "__main__":
    # USDT paritesine sahip sembolleri al
    usdt_symbols = get_usdt_symbols()
    # Tarih ve saat bilgisini istediğiniz formatta yazdırın
    print("Şu anki tarih ve saat:", simdi)
    # RSI değeri 29'un altında olan coinleri listele
    print("RSI değeri 29'un altında olan coinler:")
    for symbol in usdt_symbols:
        rsi = get_rsi(symbol)
        if rsi < 29:
            print(f"{symbol}: RSI={rsi}")
