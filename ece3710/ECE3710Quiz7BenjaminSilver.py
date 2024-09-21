meanX = 10
meanY = 30
stdvX = 1
stdvY = 2

print("For Problem 1:")

# a)
meanZ1 = (2 * meanX) + (2 * meanY)
stdvZ1 = (2 * stdvX) + (2 * stdvY)
varZ1 = meanZ1 - stdvZ1
print("For Part A:")
print("The Mean of Z1 is: ", meanZ1)
print("The Variance of Z1 is: ", varZ1)
print("The Standard Deviation of Z1 is: ", stdvZ1)

# b)
meanZ2 = meanX - (3 * meanY) + 1
stdvZ2 = stdvX - (3 * stdvY) + 1
varZ2 = meanZ2 - stdvZ2
print("For Part B:")
print("The Mean of Z2 is: ", meanZ2)
print("The Variance of Z2 is: ", varZ2)
print("The Standard Deviation of Z2 is: ", stdvZ2)


