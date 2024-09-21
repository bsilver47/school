import numpy as np
import matplotlib.pyplot as plt

x = []
fofxlist = []
for j in range(200):
    i = (j / 100)
    x.append(i)
    if (i >= 0) and (i <= 1):
        fofx = (1 - i)  
    else:
        fofx = 0
    fofxlist.append(fofx)

sum = 0
counter = 0
for i in x:
    sum += i
    counter += 1
mean = sum / counter
print("Mean: ", mean)

stdev = 0
for i in x:
    stdev += ((i - mean) ** 2)
stdev = stdev / counter

vals, bins = np.hist(x, bin=10)
pdf = vals / sum(vals)
cdf = np.cumsum(pdf)

plt.plot(bins[1:], pdf, color="blue", label="PDF")
plt.plot(bins[1:], cdf, label="CDF")
plt.legend()

