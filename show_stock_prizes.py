import matplotlib
import matplotlib.pyplot as plt
import os

from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

param = {
    'q': "ASELS", # Stock symbol (ex: "AAPL")
    'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
    'x': "IST", # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "1Y" # Period (Ex: "1Y" = 1 year)
}
asels = get_price_data(param)
plt.title('Opening stock prices for IST: ASELS')
plt.plot(asels['Open'])
plt.show()

