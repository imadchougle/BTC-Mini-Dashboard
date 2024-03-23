from flask import Flask, jsonify, send_file
import pymongo

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["btc_database"]
mycol = mydb["candle_data"]


@app.route('/api/candle_data')
def get_candle_data():
    cursor = mycol.find({}, {'_id': 0, '0': 1, '1': 1, '2':2, '3':3, '4':4})
    candle_data = list(cursor)
    formatted_data = [[row['0'], row['1'], row['2'], row['3'], row['4']] for row in candle_data]
    return jsonify(formatted_data)


@app.route('/')
def chart():
    return send_file('chart.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8000)