import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


print("1.)"
x1 = [1, 2, 3, 4, 5, 6, 7]
y1 = [2, 1, 4, 3, 7, 5, 6]
n1 = 7
aveX1 = sum(x1) / len(x1)
aveY1 = sum(y1) / len(y1)
stdvX1 = np.std(x1)
stdvY1 = np.std(y1)
covar1 = stdvX1 * stdvY1 / n1
cro1 = (covar1/stdvX1)*(stdvY1/covar1)
vro1 = np.corrcoef(x1,y1)
err1 = abs(vro1[0,1]-cro1)
print("The calculated Correlation Coefficient is:", round(cro1, 4))
print("The verified Correlation Coefficient is:", round(vro1[0,1], 4))
print("This means there was an error of:", round(err1, 4))

print("2.)")
n2 = 16
temp2 = [110, 110, 111, 111, 112, 112, 114, 114, 117, 117, 122, 122, 130, 130, 143, 143]
srate2 = [30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]
yield2 = [70.27, 72.29, 72.57, 74.69, 76.09, 73.14, 75.61, 69.56, 74.41, 73.49, 79.18, 75.44, 81.71, 83.03, 76.98, 80.99]
a2 = np.corrcoef(temp2,yield2)
b2 = np.corrcoef(srate2,yield2)
c2 = np.corrcoef(temp2,srate2)
print("a.) The correlation between temperature and yield is: ", round(a2[0,1], 4))
print("b.) The correlation between stirring rate and yield is: ", round(b2[0,1], 4))
print("c.) The correlation between temperature and stirring rate is: ", round(c2[0,1], 4))
