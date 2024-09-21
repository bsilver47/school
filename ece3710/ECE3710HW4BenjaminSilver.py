
# Q1
# X ~ Bin(7,0.3)
# a) p(X = 2)
a1 = 7 * (0.3 ** 2) * (0.7 ** 2)
print("1a: ", a1)
# b) p(X < 1)
b1 = 1 - (0.3 ** 7) - 7 * (0.3 ** 1) * (0.3 ** 6) - 7 * (0.3 ** 2) * (0.3 ** 5) 
print("1b: ", b1)
# c) p(X > 4)
c1 = 1 - (0.3 ** 7) - 7 * (0.3 ** 1) * (0.3 ** 6) - 7 * (0.3 ** 2) * (0.3 ** 5)
print("1c: ", c1)
# d) meanx
d1 = (7 + 0.3) / 2
print("1d: ", d1)

# Q2 Probabilities of
# a) p(X = 2) when X ~ Bin(4,0.6)
# b) p(X > 2) when X ~ Bin(8,0.2)
# c) p(3<= X <= 5) when X ~ Bin(6,0.7)

# Q3 X ~ Poisson(4)
# a) p(X = 1)
# b) p(X < 2)
# c) meanx
# d) stdv

