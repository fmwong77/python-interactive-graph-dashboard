from bokeh.plotting import figure
from bokeh.io import output_file, show

# prepare some data
x = [1,2,3,4,5]
y = [6,7,8,9,10]

output_file("line.html")

# create figure object
f = figure()
# create line plot
f.line(x,y)
show(f)