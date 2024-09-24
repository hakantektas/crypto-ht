# RSI Value Check Project on Binance USDT Pairs

📌 This project contains a Python script that checks the RSI (Relative Strength Index) values of coins in the USDT pairs on the Binance crypto exchange.

📌 It was created to check the RSI values of coins traded in the USDT pair on the Binance crypto exchange.

📌 This script checks the RSI (Relative Strength Index) values of all cryptocurrencies with the USDT pair listed on the Binance exchange. RSI is a technical indicator used to determine whether an asset is overbought or oversold.

📌 The script analyzes the price changes for each cryptocurrency over a certain period (here 14 hours). As a result of this analysis, it identifies cryptocurrencies whose RSI value falls below 29 and and RSI value rising above 80 on the daily timeframe. This may indicate that the price of that cryptocurrency is oversold.

🛑 "This application is not investment advice. Any decision regarding its use must be made by the user. Do your own research or consult a financial advisor before investing."

📖 Usage/Examples/Requirements

📦 **1. Python Installation:** This script is written in Python 3. Make sure you have Python 3 installed on your computer.

🚀 **Features**

📌 RSI (Relative Strength Index) is a technical indicator used to analyze the rate and magnitude of price change of an asset.

📌 This Python script calculates the RSI value for each USDT pair and prints the ones with an RSI value below 29.

📌 To do this, it uses the Binance API and fetches the last 14 hours of closing prices for each coin.

📌 Finally, it calculates the RSI value and if it's below 29 and RSI value rising above 80 on the daily timeframe, it prints the coin's symbol and RSI value on the screen.

📌 By running this script, you can list the coins in the USDT pair on the Binance crypto exchange that have an RSI below 29.

📌 Data are taken as 4-hour candlesticks.

📌 14 is the period used to calculate the RSI (Relative Strength Index). To calculate the RSI, the average gain and average loss values of price changes over a given period are usually calculated. This period refers to a time frame used to analyze the price changes of an asset.

📌 For example, in a period of 14, the price changes of the last 14-hour candlestick are taken into account. This is used in the RSI calculation to calculate the average gain and average loss of the last 14 hours of price movements.

📌 The length of the period can vary depending on the asset being analyzed and the timeframe used. 14 is used here because RSI traditionally has a default setting of 14 periods.

**Remarks**

📌  ```get_rsi**(symbol, interval='1d'):```Uses daily (1d) timeframe for RSI calculation. ```limit=14```, gets 14 days of closing prices.

📌  ```get_usdt_symbols():``` Retrieves all symbols with the USDT pair from the Binance API.

📌  **Results:** ```Coins with RSI below 29:``` and ```Coins with RSI above 80: ```lists cryptocurrencies with RSI values in the specified range.

📦 **Setup**

Open a new terminal window and clone the Project

```bash {"id":"01HWTY2MR21TNQYS436JHZMKWG"}
  git clone https://github.com/hakantektas/crypto-ht.git
```

Navigate to the project directory

```bash {"id":"01HWTY2MR21TNQYS436K5X2CEA"}
  cd crypto-ht
```

Install the required packages
Install crypto-ht using npm

```bash {"id":"01HWTY2MR21TNQYS436NZV41TM"}
  npm i crypto-ht
```

Run to list cryptocurrencies with an RSI of 29 and below for the USDT pair and RSI value rising above 80 on the daily timeframe

```bash {"id":"01HWTY2MR21TNQYS436RK8VA5D"}
  npm run getRSI
```

Run to pull all USDT pairs from the Binance exchange and print them to a file in JSON format

```bash {"id":"01HWTY2MR21TNQYS436TH57CVF"}
  npm run getSymbol
```

📊 Displaying Results:** The script prints the symbols and RSI values of coins with RSI below 29 and RSI value rising above 80 on the daily timeframe.
🚀 **Technologies Used**

This script is written in Python 3 and built with a GPT-3 based helper provided by  [OpenAI](https://openai.com/)

Binance APIs are used. For more information, please refer to the [Binance API](https://binance-docs.github.io/apidocs/spot/en/#introduction)

🛠️ **Python Setup**

Make sure you have Python 3 installed on your computer, you can install it by following the steps below.

🖥️ **Windows**

⬇️ **1. Download from Python.org:**
Download Python 3 for Windows from Python.org, the official website of Python. You can find the download page here.

📦**2. Installation:**
Install Python 3 by running the downloaded file. During installation, you can check the "Add Python 3.x to PATH" option to have Python automatically added to the PATH variable.

✅ **3. Check:**
To make sure that Python is installed correctly, open a command prompt (Command Prompt) and enter the following command:

```sh {"id":"01HWTY2MR21TNQYS436XB43MQ2"}
python --version
```

🍎 **macOS**

📦 **1. Installation with Homebrew:**

If Homebrew is not installed, install Homebrew first:

```sh {"id":"01HWTY2MR21TNQYS436Z1C1JRV"}
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Next, install Python 3 using the following command:

```sh {"id":"01HWTY2MR21TNQYS43702VRD9D"}
brew install python
```

✅ **2. Check:**
To make sure Python is installed correctly, open a terminal and enter the following command:

```sh {"id":"01HWTY2MR21TNQYS43715B9DCT"}
python3 --version
```

This command will print the version number of Python installed.

🐧 **Linux (Ubuntu/Debian)**

📦 **1. Install with Apt:**
Open Terminal and install Python 3 using the following command:

```sh {"id":"01HWTY2MR3HTAG84CC1KACCH4M"}
sudo apt update
sudo apt install python3
```

✅ **2. Check::**
To make sure Python is installed correctly, open a terminal and enter the following command:

```sh {"id":"01HWTY2MR3HTAG84CC1PHPXGBQ"}
python3 --version
```

This command will print the version number of Python installed.
Following these steps, you can easily install Python 3 on your operating system.

🤝 **Contributing**

If you would like to contribute to this project, please open a GitHub issue or submit a pull request.

🛑  Disclaimer

This application does not offer investment advice and states that any financial decision should be made by the user. The developers do not accept any responsibility for the use of the project.

📸 Screenshots

![Application Screenshot](././consoleApp.png)
