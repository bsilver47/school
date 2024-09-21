import numpy
from pomegranate import * # GaussianKernelDensity #, plot

x = [2.48, 7, 6.45, -0.79, 0.35, 4.67, 1.6, 6.68, -2.43, 3.36, 2.44, 7.96]

summary = 0
counter = 0
for i in x:
    summary += i
    counter += 1
mean = summary / counter
print("Mean: ", mean)
numerator = 0
for i in x:
    numerator += ((i - mean) ** 2)
variance = numerator / counter
print("Variance: ", variance)
gaussian_distribution = GaussianKernelDensity(mean, variance)
print("Gaussian Distribution: ", gaussian_distribution)
pdfplotter = pomegranate.distributions.plot(gaussian_distribution)

