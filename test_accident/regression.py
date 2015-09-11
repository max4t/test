import numpy as np
from scipy.optimize import minimize


def linearCostFunction(X, y, theta, lambd):

	m = len(y)
	J = 0

	hy = X * theta - y
	J = (hy.transpose() * hy + lambd * theta[1:].transpose() * theta[1:]) / (2 * m)

	temp = theta;
	temp[0, 0] = 0;

	grad = (X.transpose() * hy + lambd * temp) / m;

	return (J[0, 0], grad[:, 0])

def logisticCostFunction(X, y, theta, lambd):
	m = len(y)
	h = sigmoid(X.dot(theta))
	J = (-y.transpose().dot(np.log(h)) - (-y + 1).transpose().dot(np.log(-h + 1))) / m + np.sum(np.power(theta[:, 1:], 2)) * lambd
	reg = theta / m * lambd
	reg[0, 0] = 0
	grad = X.transpose().dot((h - y)) / m + reg
	return (J[0, 0], grad[:, 0])

def sigmoid(z):
	return np.divide(1, np.exp(-z) + 1)

def logisticOptimize(X, y, theta0, lambd):
	fct = lambda theta: (logisticCostFunction(X, y, np.matrix(theta).transpose(), lambd)[0])
	res = minimize(fct, theta0, options={'maxiter': 400})
	if not res.success:
		return (None, None)
	return (res.x, fct(res.x))


if __name__ == "__main__":
	import scipy.io
	print("#### Ex2 reg ####")
	data = np.loadtxt('ex2data2.txt', delimiter=',')
	X = data[:, :2]
	y = data[:, 2:]#np.hstack((np.ones((X.shape[0], 1)), X))
	theta = np.ones((X.shape[1], 1))
	res = logisticCostFunction(X, y, theta, 1)
	print("Res: 0.693147")
	print(res[0])
	print("---------")
	print("Res: [1.8788e-02 7.7771e-05]")
	print(res[1])
	X = data[:, :2]
	y = data[:, 2:]#np.hstack((np.ones((X.shape[0], 1)), X))
	theta = np.zeros((X.shape[1], 1))
	theta, J = logisticOptimize(X, y, theta, 1)
	print("---------")
	print("Res: [-0.307250 -0.024319]")
	print(theta)
	print("---------")
	print("Res: 0.69027")
	print(J)





