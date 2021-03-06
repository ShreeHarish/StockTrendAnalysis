import datetime as dt
import json
import os
import urllib.request
import pandas as pd

api_key = 'OLM3WDSGIJEUF4AP'
ticker = 'AAPL'
url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s" % (
    ticker, api_key)
file_to_save = 'stock_market_data-%s.csv' % ticker

if not os.path.exists(file_to_save):
    with urllib.request.urlopen(url_string) as url:
        data = json.loads(url.read().decode())

        data = data['Time Series (Daily)']
        df = pd.DataFrame(columns=['Date', 'Low', 'High', 'Close', 'Open'])
        for k, v in data.items():
            date = dt.datetime.strptime(k, '%Y-%m-%d')
            data_row = [date.date(), float(v['3. low']), float(v['2. high']),
                        float(v['4. close']), float(v['1. open'])]
            df.loc[-1, :] = data_row
            df.index = df.index + 1
    print('Data saved to : %s' % file_to_save)
    df.to_csv(file_to_save)


