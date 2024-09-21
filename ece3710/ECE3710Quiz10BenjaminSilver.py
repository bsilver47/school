# Benjamin Silver
# ECE 3710
# Quiz 10

import numpy as np
from scipy import optimize

x = [1, 2, 3]
x = np.transpose(np.array(x))
x_aug = [1, -1, 3, 2, 1, 2, 3]
y = [1.8, 3.9, 6.2]
y = np.transpose(np.array(y))
ab = np.transpose(np.array(['a', 'b']))
e = np.transpose(np.array(['e1', 'e2', 'e3']))

def lineary(a, b):
    ly = a*x + b
    return ly

print('1.')
print('a)')
print(y, '=', x, '*', ab, '+', e)
# beta = np.linalg.inv(x_aug * x_aug)*x_aug*y

print('b)')
b1 = "2.2 - 0.433 * x" # work on paper
print(b1)

print('c)')
aveX1 = sum(x) / len(x)
aveY1 = sum(y) / len(y)
stdvX1 = np.std(x)
stdvY1 = np.std(y)
covar1 = stdvX1 * stdvY1 / 3
cro1 = (covar1/stdvX1)*(stdvY1/covar1)
vro1 = np.corrcoef(x,y)
err1 = abs(vro1[0,1]-cro1)
print(err1)

