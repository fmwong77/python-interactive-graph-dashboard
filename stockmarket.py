import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
from bokeh.plotting import figure, show, output_file


start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2016, 3, 10)

df = web.DataReader("GOOG", 'yahoo', start, end)
df.tail()

p = figure(title="Candlestick Chart", x_axis_type='datetime', width=1000, height=300)
p.grid.grid_line_alpha = 0.3
hours_12 = 12*60*60*1000 # to get milisecond

def status(open, close):
    if open > close:
        value = "Decrease"
    elif open < close:
        value = "Increase"
    else:
        value = "Equal"

    return value

df["Status"] = [status(o, c) for o, c in zip(df.Open, df.Close)]
df["Middle"] = (df.Open+df.Close) / 2
df["Height"] = abs(df.Open-df.Close)

print(df)

p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12, df.Height[df.Status == "Increase"],
    fill_color="green", line_color="black")

p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12, df.Height[df.Status == "Decrease"],
    fill_color="red", line_color="black")

output_file("candlestick.html")
show(p)