import requests
from datetime import datetime

# Get current date and time
simdi = datetime.now()

def get_rsi(symbol, interval='1d'):
    """Belirtilen sembol için RSI hesaplar (günlük zaman diliminde)."""
    # Binance API endpoint (1 günlük mum verileri)
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit=14"

    try:
        # Binance API'den veri al
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Kapanış fiyatlarını al
        closes = [float(entry[4]) for entry in data]

        # RSI hesaplaması
        gains = [closes[i + 1] - closes[i] for i in range(len(closes) - 1) if closes[i + 1] > closes[i]]
        losses = [-1 * (closes[i + 1] - closes[i]) for i in range(len(closes) - 1) if closes[i + 1] < closes[i]]

        avg_gain = sum(gains) / 14
        avg_loss = sum(losses) / 14

        if avg_loss == 0:
            return 100

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        return rsi

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching RSI for {symbol}: {e}")
        return None

def get_usdt_symbols():
    """USDT paritesine sahip sembolleri getirir."""
    # Binance API endpoint
    url = "https://api.binance.com/api/v3/exchangeInfo"

    try:
        # Binance API'den sembolleri al
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # USDT paritesine sahip sembolleri filtrele
        usdt_symbols = [symbol['symbol'] for symbol in data['symbols'] if symbol['quoteAsset'] == 'USDT']
        return usdt_symbols

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching USDT symbols: {e}")
        return []

if __name__ == "__main__":
    # USDT paritesine sahip coinleri getir
    usdt_symbols = get_usdt_symbols()

    # Tarih ve saat bilgisini yazdır
    print("Current date and time:", simdi)

    # RSI'si 29'un altında olan coinleri listele
    print("Coins with RSI below 29:")
    for symbol in usdt_symbols:
        rsi = get_rsi(symbol)
        if rsi is not None and rsi < 29:
            print(f"{symbol}: RSI={rsi:.2f}")

    # RSI'si 80'in üstünde olan coinleri listele
    print("\nCoins with RSI above 80:")
    for symbol in usdt_symbols:
        rsi = get_rsi(symbol)
        if rsi is not None and rsi > 80:
            print(f"{symbol}: RSI={rsi:.2f}")
