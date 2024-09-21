# Benjamin Silver
# ECE 3710
# HW 5


a1 = 1.96 # alpha = 0.95
print("1. a) ", a1)
b1 = 2.33 # alpha = 0.98
print("1. b) ", b1)
c1 = 2.58 # alpha = 0.99
print("1. c) ", c1)
d1 = 1.28 # alpha = 0.8
print("1. d) ", d1)

total2 = 120 # Amp hrs
average2 = 178
stdv2 = 14
za2 = 1.96 # alpha = 0.95
# mu +/- z*stdv/sqrt(n)
plusa2 = average2 + (za2 * (stdv2 / (total2 ** (1/2))))
minusa2 = average2 - (za2 * (stdv2 / (total2 ** (1/2))))
a2 = [minusa2, plusa2]
print("2. a) ", a2)
zb2 = 2.58 # alpha = 0.99
plusb2 = average2 + (zb2 * (stdv2 / (total2 ** (1/2))))
minusb2 = average2 - (zb2 * (stdv2 / (total2 ** (1/2))))
b2 = [minusb2, plusb2]
print("2. b) ", b2)

a3 = 1.782 # alpha = 0.90 # sample size = 12
print("3. a) ", a3)
b3 = 2.365 # alpha = 0.95 # sample size = 7
print("3. b) ", b3)

a4 = 0.95 # t = 2.776 # sample size = 5
print("4. a) ", a4)
b4 = 0.80 # t = 1.325 # sample size = 21
print("4. b) ", b4)

n5 = 30
dist5 = 10
stdv5 = 2
c5 = 0.9
z5 = 1.645
plusmean5 = c5 - (z5 * (stdv5 / (n5 ** (1/2))))
minusmean5 = c5 + (z5 * (stdv5 / (n5 ** (1/2))))
mean5 = [plusmean5, minusmean5]
print("5. ", mean5)

n6 = 10
dist6 = 10
stdv6 = 2
c6 = 0.9
t6 = 1.813
plusmean6 = c6 - (t6 * (stdv6 / (n6 ** (1/2))))
minusmean6 = c6 + (t6 * (stdv6 / (n6 ** (1/2))))
mean6 = [plusmean6, minusmean6]
print("6. ", mean6)
