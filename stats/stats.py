import scipy.misc as misc
import numpy as np
import time





'''
    compute square root of n

    # Stop iterating when the new 
    approximation is within PRECISION of the old value.
'''


def sqrt(n):
    x_i = 20
    precision = 0.000000001

    xi_plus = 21
    while abs(xi_plus - x_i) > precision:
        x_i = xi_plus
        xi_plus = (x_i + n / x_i) / 2.0

    return xi_plus


'''
    find the mean of an iterable 
    data structure of floats or integers
    
    :param data
'''


def means(x):
    total = 0.0
    for num in x:
        total += num

    return total / len(x)


'''
    sum of the difference from mean, squared
    
    :param data
'''


def var(x):
    total_variance = 0.0
    mean = means(x)
    for num in x:
        total_variance += (num - mean) ** 2

    return total_variance / len(x)


'''
    find the covariance for two data
    sets

    :param x, y
'''


def cov(x, y):
    x_bar = means(x)
    y_bar = means(y)

    total_covariance = 0.0

    for i in range(len(x)):
        total_covariance += (x[i] - x_bar) * (y[i] - y_bar)

    return total_covariance / len(x)


SEED = int(round(time.time() * 1000)) # initial seed
GLOBAL_X_PLUS1 = 0 # x_plus1 from every call of runif01()


'''
    random uniform number generator
    
    :return float between 0 and 1
'''


def runif01():
    a = 7 ** 5
    m = 2 ** 31 - 1

    global GLOBAL_X_PLUS1

    if GLOBAL_X_PLUS1 == 0:
        x_n = SEED
    else:
        x_n = GLOBAL_X_PLUS1

    GLOBAL_X_PLUS1 = a * x_n % m

    return GLOBAL_X_PLUS1 / float(m)
    

'''
    runif returns an integer between 
    start and end 
    
    :param start, end 
'''


def runif(start, end):
    multiplier = runif01()
    x_nplus1 = int(start + (end - start) * multiplier)

    return x_nplus1


'''
    binomial random number generator
    
    :param n, p
'''


def binomial(n, p):
    successes = 0
    for i in range(n):
        rand_var = runif01()
        if rand_var < p:
            successes += 1

    return successes


'''
    binom...
'''


def binom(n, k, p):
    comb = misc.comb(n, k)
    return comb * (p ** k) * (1 - p) ** (n - k)


'''
    random exponetial number generator
'''


def rexp(lambduh):
    u = runif01()
    return -np.log(1 - u)/lambduh


'''
    exponential probability distribution function
'''


def exppdf(x, lambduh):
    return lambduh*np.exponential(-lambduh * x)


'''
    set_seed sets the seed to determine 
    the sequence of pseudo random variables 
    that will be generated 
'''


def set_seed(s):
    global GLOBAL_X_PLUS1
    global SEED

    if GLOBAL_X_PLUS1 == 0:
        SEED = s
    else:
        a = 7 ** 5
        m = 2 ** 31 - 1
    GLOBAL_X_PLUS1 = a * s % m


'''
   probability density function for 
   normal distribution 
'''


def normpdf(x, mu, sigma):
    return 1 / (sigma * sqrt(2 * np.pi)) * (np.exp((-(x-mu)**2) / (2 * sigma**2)))


'''
    uniform variance 
'''


def unifvar(a, b):
    return (b - a)**2 / 12.0










