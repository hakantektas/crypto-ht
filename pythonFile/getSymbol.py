import requests
import json

def get_usdt_symbols():
    # Binance API endpoint
    url = "https://api.binance.com/api/v3/exchangeInfo"
    
    # Get symbols from the Binance API
    response = requests.get(url)
    data = response.json()
    
    # Filter symbols with USDT pair
    usdt_symbols = [symbol['symbol'] for symbol in data['symbols'] if symbol['quoteAsset'] == 'USDT']
    
    return usdt_symbols

def write_to_json_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    usdt_symbols = get_usdt_symbols()
    write_to_json_file(usdt_symbols, 'usdt_symbols.json')
    print("Symbols with USDT parity were successfully written to the JSON file.")
