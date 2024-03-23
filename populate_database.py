import pymongo
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["btc_database"]
mycol = mydb["candle_data"]

binance_api_url = "https://api.binance.com/api/v3/klines"
symbol = "BTCUSDT"
interval = "1d"
limit = 1000

mycol.delete_many({})

params = {
    'symbol': symbol,
    'interval': interval,
    'limit': limit
}
response = requests.get(binance_api_url, params=params)

if response.status_code == 200:
    data = response.json()

    formatted_data = [{str(i): val for i, val in enumerate(row)} for row in data]
    mycol.insert_many(formatted_data)

    print("Data inserted successfully into MongoDB.")
else:
    print("Failed to fetch data from Binance API.")
