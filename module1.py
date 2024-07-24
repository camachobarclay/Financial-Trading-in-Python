import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import bt

# Load the data

bitcoin_data = pd.read_csv("bitcoint_data.csv", index_col = 'Data', parse_dates = True)
print(bitcoin_data.head())

# plot closing price data
plt.plot(bitcoin_data['Close'], color = 'red')
plt.title("Daily close price")
plt.show()

# Define a candlestick
candlestick = go.Candlestick(
	x = bitcoin_data.index,
	open = bitcoin_data['Open'],
	high = bitcoin_data['High'],
	low = bitcoin_data['Low'],
	close = bitcoin_data['Close'])
# Create a plot
fig = go.Figure(data = [candlestick])
fig.show()

# Resample from hourly to daily
eurusd_daily = eurusd_h.resample('D').mean()
eurusd_weekly = eurusd_h.resample('W').mean()

#Calculate daily returns
stock_data['daily_returns'] = stock_data['Close'].pct_change()*100
plt.plot(stock_data['daily_return'])
plt.show()
stock_data['daily_return'].hist(bins = 100)
plt.show()
stock_data['sma_50'] = stock_data['Close'].rolling(window = 50).mean()

plt.plot(stock_data['Close'], label = 'Close')
plt.plot(stock_data['sma_50'], label = 'SMA_50')
plt.legend()
plt.show()

bt_data = bt.get('goog','amzn','tsla', start = '2020-6-1', end = '2020-12-1')
print(bt_data.head())

bt_strategy = bt.Strategy('Trade_Weekly', 
							[bt.algos.RunWeekly(), # Run weekly)
							 bt.algos.SelectAll(), # Use all data
							 bt.algos.WeighEqually(), # Maintain equal weights
							 bt.algos.Rebalance()]) # Rebalance

bt_test = bt.Backtest(bt_strategy, bt_data)

# Run the backtest
bt_res = bt.run(bt_test)
bt_res.plt(title = "Backtest result")
bt_res.get_transactions()