import pandas as pd
import yfinance as yf

tickers_df = pd.read_csv('./data/indices.csv')
indices = tickers_df.ticker.unique()
data = yf.download(" ".join(indices),
                   start="2018-01-01", end="2023-01-01",
                   interval = "1d",
                   prepost=False,
                   repair = True
)

data['Close'].to_csv('./data/raw_data.csv')