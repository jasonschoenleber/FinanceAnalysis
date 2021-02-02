# Python script to create candlestick chart using plotly for any stock ticker min-to-min with high/low markers
# Alpha Vantage API Key = J54L4V2W2HSQMWZK
# Imports that you are going to need to read a file
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from datetime import date
import time
# Import library to create chart
# To build the chart we need to give the candlestick chart the X axis and multiple points on the Y axis.
# We do this with the graph_objs
import plotly.graph_objs as go


# Add api key variable
api_key = 'J54L4V2W2HSQMWZK'

# Specify output format
ts = TimeSeries(key = api_key, output_format = 'pandas')

# Set variables and pass in the ticker, interval, and output size
ba, meta_data = ts.get_intraday(symbol='NKLA', interval = '1min', outputsize = 'full')
# ba, meta_data = ts.get_daily(symbol='NKLA', outputsize = 'full')

# Specify start date
today = date.today()
ba_date_changed = ba[:today]
print(ba_date_changed)

# Create CSV export
ba_date_changed.to_csv("NKLA.csv")

# Read the file using pandas
df_BA_bar_Data = pd.read_csv("NKLA.csv")

# Show some of the data you read
df_BA_bar_Data.head()

# Find and set variables for min and max values
low_px = df_BA_bar_Data['4. close'].min()
low_ind = df_BA_bar_Data['4. close'].idxmin()
low_time = df_BA_bar_Data.loc[low_ind,'date']
high_px = df_BA_bar_Data['4. close'].max()
high_ind = df_BA_bar_Data['4. close'].idxmax()
high_time = df_BA_bar_Data.loc[high_ind,'date']
print(low_time, high_time)

# Adding annotations for ther high and low of the day
annotations = []
annotations.append(go.layout.Annotation(x=low_time,
                                        y=low_px,
                                        showarrow=True,
                                        arrowhead=1,
                                        arrowcolor="blue",
                                        arrowsize=2,
                                        arrowwidth=2,
                                        text="Low"))

annotations.append(go.layout.Annotation(x=high_time,
                                        y=high_px,
                                        showarrow=True,
                                        arrowhead=1,
                                        arrowcolor="blue",
                                        arrowsize=2,
                                        arrowwidth=2,
                                        text="High"))

# Create a basic layout that names the chart and each axis.
layout = dict(
        title="BA",
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title( text="Time (EST - New York)"), rangeslider=dict (visible = True)),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title( text="Price - $")),
        width=1000,
        height=800,
        annotations=annotations
)

# Set the data from our data frame
data=[go.Candlestick(x=df_BA_bar_Data['date'],
                open=df_BA_bar_Data['1. open'],
                high=df_BA_bar_Data['2. high'],
                low=df_BA_bar_Data['3. low'],
                close=df_BA_bar_Data['4. close'])]

# Display the candlestick chart with the optional layout
figSignal = go.Figure(data=data, layout=layout)
figSignal.show()
