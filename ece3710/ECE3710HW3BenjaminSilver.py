# Question 1:
print("This marks the beginning of the answers to question 1")
sig_x = 0.3
sig_y = 0.2

a1 = 4 * sig_x
print("The answer to a is: ", a1)
b1 = (sig_x) + (2 * sig_y)
print("The answer to b is: ", b1)
c1 = (2 * sig_x) - (3 * sig_y)
print("The answer to c is: ", c1)
d1 = (2 * sig_x) - (3 * sig_y) + 2
print("The answer to d is: ", d1)

# Question 2:
print("This marks the beginning of the answers to question 2")
x = [-2, -1, 0]
y = [1, 3, 5]

def z_1(x, y):
    z = x - (2 * y)
    return z

a2_sum = 0
a2_counter = 0
for i in x:
    for j in y:
        runvar = z_1(i, j)
        a2_sum += runvar
        a2_counter += 1
a2_mean = a2_sum / a2_counter
print("The mean of a is: ", a2_mean)
a2_sig = 0
for i in x:
    for j in y:
        runvar = z_1(i, j)
        a2_sig += ((runvar - a2_mean) ** 2)
a2_var = a2_sig / a2_counter
print("The variance of a is: ", a2_var)
a2_stdev = a2_var ** (1/2)
print("The standard deviation of a is: ", a2_stdev)

def z_2(x, y):
    z = x + (2 * y) + 1
    return z

b2_sum = 0
b2_counter = 0
for i in x:
    for j in y:
        runvar = z_2(i, j)
        b2_sum += runvar
        b2_counter += 1
b2_mean = b2_sum / b2_counter
print("The mean of b is: ", b2_mean)
b2_sig = 0
for i in x:
    for j in y:
        runvar = z_2(i, j)
        b2_sig += (runvar - b2_mean) ** 2
b2_var = b2_sig / b2_counter
print("The variance of b is: ", b2_var)
b2_stdev = b2_var ** (1/2)
print("The standard deviation of b is: ", b2_stdev)

