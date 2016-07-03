from stats import * 
import matplotlib.pyplot as plt

 
N = 4 
TRIALS = 500

X = []
for i in range(TRIALS):
    data = []
    for j in range(N):  
        data.append(runif01())

    X.append(means(data))

plt.hist(X, bins=40, normed=1)

mean = 0.5 
var = unifvar(0, 1) / N
x_range = np.linspace(0, 1, len(X))
Y = [normpdf(x, mean, sqrt(var)) for x in np.arange(0.0, 1.0, 0.005)]

plt.plot(np.linspace(0.0, 1.0, len(Y)), Y, '-r')

plt.show()
