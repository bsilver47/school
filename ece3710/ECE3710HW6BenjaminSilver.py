import scipy.stats as st
# Q1
n1 = 73
mean1 = 783
stdv1 = 120
# H0: mean <= 750
# H1: mean > 750
z1 = (mean1 - 750) / (stdv1 / (n1 ** 0.5))
print("Q1: ", z1)
p1 = 1 - st.norm.cdf(z1)
print(p1)
# find p-value

# Q2
oldmean2 = 5.4
n2 = 80
newmean2 = 4.5
stdv2 = 2.7
# H0: mean >= 5.4
# H1: mean < 5.4
z2 = (oldmean2 - newmean2) / (stdv2 / (n2 ** 0.5))
# find p-value
print("Q1: ", z2)


# Q3
p3 = 0.01
print("3. iii. There is a 1% probability that H0 is true.")

# Q4
rmean4 = 900.4 #Ohms
stdv4 = 4
pmean4 = 900 #Ohms
p_pval4 = 0.05
# H0: Mean = 900
# H1: Mean != 900
na4 = 4
ta4 = (rmean4 - pmean4) / (stdv4 / (na4 ** 0.5))
# find pa4 = 
# find conclusiona4 = 
print("Q4: a) ", ta4)
pa4 = (1 - st.norm.cdf(ta4)) * 2
print(pa4)

nb4 = 40
zb4 = (rmean4 - pmean4) / (stdv4 / (nb4 ** 0.5))
print("Q4: b) ", zb4)
pb4 = (1 - st.norm.cdf(zb4))
print(pb4)
