from stats import * 
import matplotlib.pyplot as plt

 
N = 4 
TRIALS = 2000


X = []
for i in range(TRIALS):
    data = []
    for j in range(N):  
        data.append(runif01())

    X.append(means(data))

mean = 0.5
var = unifvar(0, 1) / N

fig = plt.figure()
ax = fig.add_subplot(111)
plt.hist(X, bins=40, normed=1)
plt.text(.02, .9, '$N = %d$' % N, transform=ax.transAxes)
plt.text(.02, 0.85, '$TRIALS = %d$' % TRIALS, transform=ax.transAxes)
plt.text(.02, 0.80, 'mean($\\overline{X}$) = %f' % np.mean(X), transform=ax.transAxes)
plt.text(.02, 0.75, 'var($\\overline{X}$) = %f' % np.var(X), transform=ax.transAxes)
plt.text(.02, 0.7, 'var U($0,1$)/%d = %f' % (N, var), transform=ax.transAxes)

plt.title("CLT Density Demo, sample mean of U(0,1) is $N(.5, \sigma^2/N)$")
plt.xlabel("$\\overline{X}$", fontsize=16)
plt.ylabel("Density", fontsize=16)

Y = [normpdf(x, mean, sqrt(var)) for x in np.arange(0.0, 1.0, 0.005)]

plt.plot(np.linspace(0.0, 1.0, len(Y)), Y, '-r')

plt.show()
