## BTC Mini Dashboard Snapshot

![image](https://github.com/imadchougle/BTC-Mini-Dashboard/assets/54437743/464ffc99-798a-4fd7-b5da-02c4a1cda3ad)

## Introduction

The BTC Mini Dashboard web application offers several features to users for tracking cryptocurrency data and managing their investments:

1. Real-Time Candlestick Chart Visualization: Utilizes data from the Binance API to populate daily candlestick data, which is then stored in MongoDB. The application fetches this data from MongoDB and renders it into a candlestick chart using a charting library. Users can analyze market trends, patterns, and sentiments based on the graphical representation of price movements.

2. Real-Time Portfolio Tracker: Allows users to input their buying price and quantity of Bitcoin. The application calculates their total investment, current value, and profit/loss in real-time, providing insights into their investment performance.

3. Crypto Table: Fetches data from the Coin Gecko API to display a table of the top 10 cryptocurrencies by market capitalization. The table includes details such as rank, symbol, price, market cap, and 24-hour price change, enabling users to stay informed about the current state of the cryptocurrency market.

4. Currency Converter: Enables users to convert a specified amount of Bitcoin into different fiat currencies (USD, INR, AED) based on the current exchange rates. It also calculates the converted amount, providing users with the flexibility to assess their holdings in various fiat currencies.

5. Live Cryptocurrency Returns: Users can view live cryptocurrency returns for different time intervals (7 days, 1 month, 6 months, and 1 year), allowing them to track the performance of various cryptocurrencies over specific periods.

## Dependencies

- Python Flask: Flask Server works in backend

- Binance API: Utilized for retrieving cryptocurrency data.

- MongoDB: Used as the database to store cryptocurrency data fetched from the Binance API.

- Coin Gecko API: Rendering the Top 10 crypto currency.

- Trading View Lightweight Charts Library: The Lightweight Charts library is used for rendering the candlestick chart. 

- Font Awesome and SVG Icons: Font Awesome and SVG icons are utilized for displaying cryptocurrency symbols.
