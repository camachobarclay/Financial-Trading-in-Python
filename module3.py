import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import bt
import talib

# Get thr price data by the stock ticker
price_data = bt.get('aapl', start = '2019-11-1', end = '2020-12-1')

# Calculate SMA
sma = price_data.rolling(20).mean()

sma = talib.SMA(price_data['Close'], timeperiod = 20)
bt_strategy = bt.Strategy('AboveEMA',
					[bt.algos.SelectWhere(price_data > sma),
					bt.algos.WeighEqually(),
					bt.algos.Rebalance()])

# Create the backtest and run its
bt_backtest = bt.Backtest(bt_strategy, price_data)
bt_result = bt.run(bt_backtest)

# Plot the backtest result
bt_result.plot(title = 'Backtest result')

EMA_short = talib.EMA(price_data['Close'],
	timeperiod = 10).to_frame()
EMA_long = talib.EMA(price_data['Close'],timeperiod = 40).to_frame()

# Create the signal DataFrame
signal = EMA_long.copy()
signal[EMA_long.isnull()] = 0

# Construct the signal

signal[EMA_short > EMA_long] = 1
signal[EMA_short < EMA_long] = -1

# Plot the signal, price and MAs

combined_df = bt.merge(signal, price_data, EMA_short, EMA_long)
combined_df.columns = ['Signal', 'Price', 'EMA_short', 'EMA_long']
combined_df.plot(secondary_y = ['Signal'])

# Define the strategy

bt_strategy = bt.Strategy('EMA_crossover',
	[bt.algos.WeighTarget(signal),
	bt.algos.Rebalance()])

bt_backtest = bt.Backtest(bt_strategy, price_data)
bt_result = bt.run(bt_backtest)

# PLot the backtest result

bt_result.plot(title = 'Backtest result')

stock_rsi = talib.RSI(price_data['Close']).to_frame()

# Create the same DataFrame structure as RSI
signal = stock_rsi.copy()
signal[stock_rsi.isnull()] = 0

# Construct the signal
signal[stock_rsi < 30] = 1
signal[stock_rsi > 70] = -1
signal[(stock_rsi >= 30) & (stock_rsi<=70)] = 0

# Merge data into one DataFrame
combined_df = bt.merge(signal, stock_data)
combined_df.columns = ['Signal', 'Price']
# Plot the signal with price
combined_df.plot(secondary_y = ['Signal'])

stock_rsi.plot()
plt.title('RSI')

#Define the strategy
bt_strategy = bt.Strategy('RSI_MeanReversion',
	[bt.algos.WeighTarget(signal),
	bt.algos.Rebalance()])

bt_backtest = bt.Backtest(bt_strategy, price_data)
bt_result = bt.run(bt_backtest)

# Plot the backtest result
bt_result.plot(title = 'Backtest result')




def signal_strategy(ticket, period, name, start = '2018-4-1', end = '2020-11-1'):
	# Get the data and calculate SMA
	price_data = bt.get(ticker,start = start, end = end)
	sma = price_data.rolling(period).mean()
	# Define the signal-based strategy
	bt_strategy = bt.Strategy(name,
					[bt.algos.SelectWhere(price_data > sma),
					bt.algos.WeighEqually(),
					bt.algos.Rebalance()])
	# Return the backtest
	return bt.Backtest(bt_strategy, price_data)




ticker = 'aapl'
sma20 = signal_strategy(ticker, period = 20, name = 'SMA20')
sma50 = signal_strategy(ticker, period = 50, name = 'SMA50')
sma100 = signal_strategy(ticker, period = 100, name = 'SMA100')

bt_results = bt.run(sma20, sma50, sma100)
bt_results.plot(title = 'Strategy optimization')

def buy_and_hold(ticker,name, start = '2018-11-1', end = '2020-12-1'):
	# Get the data
	price_Data = bt.get(ticker, start = start_date, end = end_date)
	# Define the benchmark strategy
	bt_strategy = bt.Strategy(name,
		[bt.algos.RunOnce(),
		bt.algos.SelectAll(),
		bt.algos.WeighEqually(),
		bt.algos.Rebalance()])
	# Return the backtest
	return bt.Backtest(bt_strategy, price_data)

	benchmark = buy_and_hold(ticker, name = 'benchmark')
	# Run all backtest and plot the results
	bt_results = bt.run(sma20, sma50, sma100, benchmark)
	bt_results.plot(title = 'Strategy benchmarking')