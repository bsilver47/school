import numpy as np

x = [184, 206, 193]
y = [185, 203, 200]

n = 3

aveX = sum(x) / len(x)
aveY = sum(y) / len(y)

stdvX = np.std(x)
stdvY = np.std(y)

covar = stdvX * stdvY / n

cro = (covar/stdvX)*(stdvY/covar)
print("The calculated Correlation Coefficient is ", round(cro, 4))

vro = np.corrcoef(x,y)
print("The verified Correlation Coefficient is ", round(vro[0,1], 4))

err = abs(vro[0,1]-cro)
print("This means there was an error of: ", round(err, 4))
