import numpy as np

np.random.seed(100)

#create array of 50 random integers between 0 and 10
var1 = np.random.randint(0, 10, 50)
#print(var1)

#create a positively correlated array with some random noise
var2 = var1 + np.random.normal(0, 10, 50)
#print(var2)

var1 = [10,20,30,40,50]
var2 = [0.5,1,1.5,2,2.5] # perfectly correlated (positive)
#var2 = [2.5,2,1.5,1,0.5] # perfectly correlated (negative)
#var2 = [0.5,1,4,2,2.5] # not well correlated

#calculate the correlation between the two arrays
#print(np.corrcoef(var1, var2))

# -1 indicates a perfectly negative linear correlation between two variables
# 0 indicates no linear correlation between two variables
# 1 indicates a perfectly positive linear correlation between two variables

print(np.corrcoef(var1, var2)[0,1])

from scipy.stats.stats import pearsonr

# test if this correlation is statistically significant
# calculate the p-value associated with the Pearson correlation coefficient
# the p-value is the second number returned
print(pearsonr(var1, var2))

# since this p-value is less than .05
# we would conclude that there is a statistically significant correlation between the two variables

import matplotlib.pyplot as plt
import numpy as np

xpoints1 = np.array([1,2,3,4,5])
ypoints1 = np.array(var1)

plt.plot(xpoints1, ypoints1)

xpoints2 = np.array([1,2,3,4,5])
ypoints2 = np.array(var2)

plt.plot(xpoints2, ypoints2)

plt.show()