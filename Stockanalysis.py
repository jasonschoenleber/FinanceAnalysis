# Alpha Vantage API Key = J54L4V2W2HSQMWZK
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'J54L4V2W2HSQMWZK'

ts = TimeSeries(key = api_key, output_format = 'pandas')
# data, meta_data = ts.get_intraday(symbol='HTZ', interval = '1min', outputsize = 'full')
data, meta_data = ts.get_daily(symbol='HTZ', outputsize = 'full')
print(data)
