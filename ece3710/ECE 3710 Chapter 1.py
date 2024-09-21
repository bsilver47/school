##import matplotlib.pyplot as plt
import math

x = [0, 1, 5, 2, 55, 39, 99, 13]

average = sum(x) / len(x)
print("The average is", average)
##plt.boxplot(x)
##plt.show()
##plt.hist(x)
##plt.show()

x.sort()
sizeX = len(x)
medianX = 0.5 * sizeX
medianX = int(medianX // 2)
xMedianX = (x[medianX + 1] + x[medianX]) / 2

print("The Median value is", xMedianX)

firstQ = 0.25 * sizeX
firstQ = int(firstQ // 2)
xFirstQ = (x[firstQ + 1] + x[firstQ]) / 2
print("The 1st Quartile value is", xFirstQ)

thirdQ = 0.75 * sizeX
thirdQ = int(thirdQ // 2)
xThirdQ = (x[thirdQ + 1] + x[thirdQ]) / 2
print("The 3rd Quartile value is", xThirdQ)

xtwofiveP = firstQ
print("The 25th percentile is", xtwofiveP)
xFiftiethP = xMedianX
print("The 50th percentile is", xFiftiethP)
sixtiethP = 0.6 * sizeX
sixtiethP = int(sixtiethP // 2)
xSixtiethP = (x[sixtiethP + 1] + x[sixtiethP]) / 2
print("The 60th percentile value is", xSixtiethP)
