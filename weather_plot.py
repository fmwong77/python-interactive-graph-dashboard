from bokeh.io import show, output_file
from bokeh.plotting import figure
import pandas

df = pandas.read_excel("http://pythonhow.com/data/verlegenhuken.xlsx")

x = df["Temperature"] / 10
y = df["Pressure"] / 10

output_file("weather.html")
f = figure(title="Temperature and Air Pressure", tools="pan")
f.xaxis.axis_label = "Temperature (°C)"
f.yaxis.axis_label = "Pressure (hPa)"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.circle(x, y, size=0.3)
show(f)
