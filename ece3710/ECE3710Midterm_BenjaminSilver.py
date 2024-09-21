import matplotlib.pyplot as plt
import numpy as np
import statistics
import random
import math
import openpyxl

# Name: Benjamin Silver
# UVU id: 10718564

array1 = [5,1,0,2,52,39,99,14]
sortedarray1 = [0,1,2,5,14,39,52,99]
a1mean = statistics.mean(array1)
print("1. a) Mean = ", a1mean)
b1median = statistics.median(sortedarray1)
print("1. b) Median = ", b1median)
c11q = np.percentile(sortedarray1, 25, interpolation = 'midpoint')
print("1. c) 1st Quartile = ", c11q)
d160p = np.percentile(sortedarray1, 60, interpolation = 'midpoint')
print("1. d) 60th Percentile = ", d160p)

array2x = [0, 1, 3, 4, 5]
array2Px = [0.1, 0.2, 0.2, 0.4, 0.1]
a2p13 = array2Px[1]
print("2. a) p(1 <= x < 3) = ", a2p13)
sum2 = 0
for i in range(len(array2x)):
    sum2 += (array2x[i] * array2Px[i] * 10)
b2mean = sum2 / 5
print("2. b) Mean = ", b2mean)
c2median = 3.5
print("2. c) Median = ", c2median)

array3 = [0,1,0,0,1,0,1,0,0,1]
sortedarray3 = [0,0,0,0,0,0,1,1,1,1]
a3y = 4/10
print("3. a) y = p(X=1) = ", a3y)
# 3b
plt.hist(array3, label = '3b')
plt.show()
#3c
plt.hist(array3, density = True, color = 'blue', label = '3c')
plt.show()

array4 = []
mu4 = 0
sigma4 = 1
for x in range(0,4):
    fx4 = (1/np.sqrt(2 * np.pi * sigma4) * math.exp(-((x-mu4)**2)/(2 * sigma4)))
    array4.append(fx4)
print("4. (Test of variables): ", array4)

array5 = [1,2,5,8,3,10,10]
mean5 = statistics.mean(array5)
sigma5 = statistics.variance(array5)
b5 = mean5 / sigma5
a5 = mean5 * b5
print("5. a = ", a5)
print("5. b = ", b5)

pa6 = 3 / 10
pb6 = 2 / 9
print("6. a) ", pa6)
print("6. b) ", pb6)
print("6. c) ", pa6+pb6)
print("6. d) ", pb6)
print("6. e) A and B are not independent because B depends on A as it is the probability of what is left after A is gone.")

print("7. a) 1")
integral7 = 2 / 3
print("7. b) ", integral7)

mean8x = 1
stdv8x = 2
mean8y = 2
stdv8y = 1
a8mean = mean8x + mean8y
b8mean = a8mean + 1
c8mean = mean8x - (2 * mean8y) - 1
a8stdv = stdv8x + stdv8y
b8stdv = a8stdv + 1
c8stdv = stdv8x - (2 * stdv8y) - 1
a8var = a8stdv
b8var = b8stdv
c8var = c8stdv
print("8. a) ")
print("Mean: ", a8mean)
print("Variance: ", a8var)
print("Standard Deviation: ", a8stdv)
print("8. b) ")
print("Mean: ", b8mean)
print("Variance: ", b8var)
print("Standard Deviation: ", b8stdv)
print("8. c) ")
print("Mean: ", c8mean)
print("Variance: ", c8var)
print("Standard Deviation: ", c8stdv)

