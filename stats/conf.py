from numpy import random
import numpy as np
import matplotlib.pyplot as plt
from stats import *

prices = []
f = open("prices.txt")
for line in f:
    v = float(line.strip())
    prices.append(v)


    '''
        Returns a random sample of data values with replacement.
        The returned array has same length as data.
    '''

def sample(data):
    rand_idx = random.randint(0, len(data), len(data))
    return [data[idx] for idx in rand_idx]

TRIALS = 20

X_list = [np.mean(sample(prices)) for x in range(TRIALS)]

X_list.sort()

lb = X_list[int(TRIALS*.025)]
ub = X_list[int(TRIALS*.975)]

inside = [lb, ub]

plot.axis([1.10, 1.201, 0, 30])
x = np.arange(1.05, 1.25, 0.001)

mean = np.mean(data)
sd = np.std(data)






