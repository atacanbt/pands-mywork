# plottask.py
# this program will plot a histogram of 1000 random values from a normal distribution with mean 5 and standard deviation 2 and a cubic function
# author: atacan buyuktalas

import numpy as np
import matplotlib.pyplot as plt

# Generating 1000 random values from a normal distribution with mean 5 and standard deviation 2
normal_values = np.random.normal(loc=5, scale=2, size=1000)
plt.hist(normal_values, color='darkorange', edgecolor='black') # histogram of the data
plt.xlabel("Value") # x-axis label
plt.ylabel("Frequency") # y-axis label
plt.title("Normal Distribution") # title of the plot
plt.show() # show the plot

# plot the function
xpoints = np.array(range(0,10)) # set the array from 0 to 10
ypoints = xpoints * xpoints * xpoints # x^3
plt.plot(xpoints, ypoints, label= "h(x)=x^3", color='blue') # plot x cubed
plt.legend() # show the label
plt.xlabel("x") # x-axis label
plt.ylabel("h(x)") # y-axis label
plt.title("Cubic Function") # title of the plot

plt.show() # show the plot