import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import bt
import talib

#calculate two SMAs

stock_data['SMA_short'] = talib.SMA(stock_data['Close']. timeperiod = 10)
stock_data['SMA_long'] = talib.SMA(stock_data['Close'], timeperiod = 50)

#print the last five rows
print(stock_data.tail())

# Plot SMA with the price
plt.plot(stock_data['SMA_short'],
	label = 'SMA_short')
plt.plot(stock_data['SMA_long'], 
	label = 'SMA_long')
plt.plot(stock_data['Close'],
	label = 'Close')

# Customize and show the plot
plt.legend()
plt.title('SMAs')
plt.show()

# Calculate two EMAs
stock_data['EMA_short'] = talib.EMA(stock_data['Close'], timeperiod = 10)
stock_data['EMA_long'] = talib.EMA(stock_data['Close'], timeperiod = 50)
#print the last five rows
print(stock_data.tail())

plt.plot(stock_data['EMA_short'],
	label = 'EMA_short')
plt.plot(stock_data['SMA_long'], 
	label = 'EMA_long')
plt.plot(stock_data['Close'],
	label = 'Close')

# Customize and show the plot
plt.legend()
plt.title('SMAs')
plt.show()

#Calculate ADX
stock_data['ADX'] = talib.ADX(stock_data['High'], stock_data['Low'], stock_data['Close'], timeperiod = 14)

#print the last five rows
print(stock_data.tail())

# Create subplots
fig, (ax1, ax2) = plt.subplots(2)

# Plot ADX with the price
ax1.set_ylabel('Price')
ax1.plot(stock_data['Close'])
ax2.set_ylabel('ADX')
ax2.plot(stock_data['ADX'])

ax1.set_title('Price and ADX')
plt.show()

#calculate RSI

stock_data['RSI'] = talib.RSI(stock_data['Close'], timeperiod = 14)

#print the last five rows
print(stock_data.tail())

fig, (ax1, ax2) = plt.subplots(2)

# Plot RSI with the price
ax1.set_ylabel('Price')
ax1.plot(stock_data['Close'])
ax2.set_ylabel('RSI')
ax2.plot(stock_data['RSI'])

ax1.set_title('Price and RSI')
plot.show()

upper, mid, lower = talib.BBANDS(stock_data['Close'],
	nbdevup = 2,
	nbdevdn = 2,
	timeperiod = 20)

plt.plot(stock_data['Close'], label = 'Price')
plt.plot(upper, label = "Upper band")
plt.plot(mid, label = 'Middle band')
plt.plot(lower,label = 'Lower band')

# Customize and show the plot
plt.title('Bollinger Bands')
plt.legend()
plt.show()

# Define the Bollinger Bands with 1-sd
upper_1sd, mid_1sd, lower_1sd = talib.BBANDS(bitcoin_data['Close'], 
                                     nbdevup = 1,
                                     nbdevdn = 1,
                                     timeperiod=20)
# Plot the upper and lower Bollinger Bands 
plt.plot(bitcoin_data['Close'], color='green', label='Price')
plt.plot(upper_1sd, color='tomato', label="Upper 1sd")
plt.plot(lower_1sd, color='tomato', label='Lower 1sd')

# Customize and show the plot
plt.legend(loc='upper left')
plt.title('Bollinger Bands (1sd)')
plt.show()