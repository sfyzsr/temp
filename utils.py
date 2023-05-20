import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd

def drawK(array):
    
    array = array.astype('float64')
    # Create a figure and an axis
    fig, ax = plt.subplots()
    # print (ax)
    # Plot the candlestick chart
    candlestick_ohlc(ax, array, width=0.6, colorup='red', colordown='green')

    # Format the x-axis to display dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()

    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('Candlestick Chart')

    # Show the plot
    plt.show()