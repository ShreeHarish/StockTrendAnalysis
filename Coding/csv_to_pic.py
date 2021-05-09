import plotly.graph_objects as go
import pandas as pd
import os

ticker = 'AAPL'
path_string = 'stock_market_data-%s' % ticker
extension = '.csv'

df = pd.read_csv(path_string + '.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'], high=df['High'],
                                     low=df['Low'], close=df['Close'])
                      ])

if not os.path.exists('images'):
    os.mkdir('images')

fig.write_image('images/' + path_string + '.png')
