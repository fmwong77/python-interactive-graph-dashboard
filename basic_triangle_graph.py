from bokeh.plotting import figure
from bokeh.io import output_file, show

# prepare some data
x = [1,2,3,4,5]
y = [6,7,8,9,10]

output_file("triangle.html")

# create figure object
f = figure()
# create triangle plot
f.triangle(x,y)
show(f)