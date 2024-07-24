import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import bt
import talib

# Get all backtest stats
resInfo = bt_result.stats
print(resInfo.index)

# Get daily, montly, and yearly returns
print('Daily return: %.4f'% resInfo.loc['daily_mean'])
print('Monthly return: %.4f'% resInfo.loc['monthly_mean'])
print('Yearly return: %.4f'% resInfo.loc['yearly_mean'])

# Get the compound annual growth rate
print('Compound annual growth rate: %.4f'% resInfo.loc['cagr'])
bt_result.plot_histograms(bins = 50, freq = 'w')

# Get the lookback return
lookback_returns = bt_result.display_lookback_returns()
print(lookback_returns)

resInfo = bt_results.stats
# Get the max drawdown
max_drawdown = resInfo.loc['max_drawdown']
print('Maximum drawdown: %.2f'% max_drawdown)
# Get the average drawdown
avg_drawdown = resInfo.loc['avg_Drawdown']
print('Average drawdown %.2f'% avg_drawdown)
# Get the average drawdown days
avg_drawdown_days = resInfo.loc['avg_drawdown_days']
print('Average drawdown days: %.0f'% avg_drawdown_days)

resInfo = bt_results.stats
# Get the CAGR
cagr = resInfo.loc['cagr']
# Get the maxdrawdown
max_drawdown = resInfo.loc['max_drawdown']

#Calculate calmar ratio manually
calmar_calc = cagr/max_drawdown*(-1)
print('Calmar Ratio calculated: %.2f'% calmar_calc)

resInfo = bt_results.stats

# Get the calmar ratio
calmar = resInfo.loc['calmar']
print('Calmar Ratio: %.2f'% calmar)

resInfo = bt_results.stats
# Get the Sharpe ratios from the backtest stats
print('Sharpe ratio daily: %.2f'% resInfo.loc['daily_sharpe'])
print('Sharpe ratio monthly %.2f'% resInfo.loc['monthly_sharpe'])
print('Sharpe ratio annually %.2f'% resInfo.loc['yearly_sharpe'])

# Obtain annual return
annual_Return = resInfo.loc['yearly_mean']
# obtain annual volatility
volatility = resInfo.loc['yearly_vol']

# Calculate Sharpe ratio manually
sharpe_ratio =  annual_return/volatility
print('Sharpe ratio annually %.2f'% sharpe_ratio)

resInfo = bt_result.stats
# Get Sortino ratio from backtest stats
print('Sortino ratio daily: %.2f'% resInfo.loc['daily_sortino'])
print('Sortino ratio monthly: %.2f'% resInfo.loc['monthly_sortino'])
print('Sortino ratio annually: %.2f'% resInfo.loc['yearly_sortino'])