from bokeh.io import output_file, show
from bokeh.plotting import figure
import pandas

df = pandas.read_csv("files\\bachelors.csv")
x = df["Year"]
y = df["Engineering"]

output_file("bachelors.html")

f = figure(plot_width=500,plot_height=400, tools='pan')
f.title.text = "Educational Data"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Year"
f.yaxis.axis_label="Engineering"    
f.line(x,y)
show(f)