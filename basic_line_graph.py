from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas 

# prepare some data
df = pandas.read_csv("files\data.csv")
x = df["x"]
y = df["y"]

output_file("line.html")

# create figure object
f = figure()
# create line plot
f.line(x,y)
show(f)