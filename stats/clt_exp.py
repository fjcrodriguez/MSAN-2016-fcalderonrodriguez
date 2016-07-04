from stats import *
import matplotlib.pyplot as plt

N = 50
TRIALS = 4000
LAMBDUH = 1.5

X = []
for i in range(TRIALS):
    data = []
    for j in range(N):
        data.append(rexp(LAMBDUH))

    X.append(means(data))

mean = LAMBDUH**(-1)
var = LAMBDUH**(-2)/N

fig = plt.figure()
ax = fig.add_subplot(111)
plt.hist(X, bins=40, normed=1)
plt.text(.02, .9, '$N = %d$' % N, transform=ax.transAxes)
plt.text(.02, 0.85, '$TRIALS = %d$' % TRIALS, transform=ax.transAxes)
plt.text(.02, 0.80, 'mean($\\overline{X}$) = %f' % np.mean(X), transform=ax.transAxes)
plt.text(.02, 0.75, 'var($\\overline{X}$) = %f' % np.var(X), transform=ax.transAxes)
plt.text(.02, 0.7, 'mean Exp($%f$) = %f' % (LAMBDUH,1/LAMBDUH), transform=ax.transAxes)
plt.text(.02, 0.65, 'var Exp($%f$)/%d = %f' % (LAMBDUH, N, (1/LAMBDUH**2)/N), transform=ax.transAxes)

plt.title("CLT Density Demo, sample mean of Exp($\lambda=1.5$ is $N(1/\lambda, (1/\lambda^2/N)$")
plt.xlabel("$\\overline{X}$", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.axis([0, 1.333, 0, 5])

Y = [normpdf(x, mean, sqrt(var)) for x in np.arange(0.0, 1.333, 0.005)]

plt.plot(np.linspace(0.0, 1.333, len(Y)), Y, '-r')
plt.savefig('clt-exp-N50-hist.pdf', format='pdf')
plt.show()
