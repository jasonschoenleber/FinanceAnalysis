# imports you will need
import datetime as dt # use to define our desired time span
import matplotlib.dates as mdates # library convert our dates into the necessary number format
import matplotlib.pyplot as plt # used for displaying the chart
import pandas_datareader as web # the module that will load the desired stock data
from mpl_finance import candlestick_ohlc # the main library for plotting

# define desired time span
start = dt.datetime(2020,1,1)
end = dt.datetime.now()

# define data reader
df = web.DataReader('NCLH', 'yahoo',start,end)

# Print Results to test we are getting the correct feedback
print(df.head())

# Select and Reorder column in the data frame
df = df[['Open', 'High', 'Low', 'Close']]

# Reset the index and convert our datetime to a number
df.reset_index(inplace=True)
df['Date'] = df['Date'].map(mdates.date2num)

# Define plots and viz data.  First define new subplot for our data, use candlestick_ohlc to plot our values, set width and colors.
ax = plt.subplot()
candlestick_ohlc(ax, df.values, width=5, colorup='g', colordown='r')
ax.xaxis_date()
ax.grid(True)
plt.show()

# Style changes to chart
ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title('NCLH Share Price', color='White')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()
