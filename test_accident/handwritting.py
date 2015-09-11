from scipy.io import loadmat
import numpy as np
from flask import Flask, json
from scipy.optimize import fmin_cg


def __prepend(X, axis = 1):
	if axis == 0:
		return np.vstack((np.ones((X.shape[1], 1)), X))
	elif axis == 1:
		return np.hstack((np.ones((X.shape[0], 1)), X))
	raise ValueError("Only handle 2D arrays")

def costFunction(theta1, theta2, X, y, lambd):
	m = X.shape[0]
	num_label = theta2.shape[0]
	res = np.zeros((len(y), num_label))
	for i in range(num_label):
		res[:, i:i+1] = (y == (i))[np.newaxis].transpose()
	res = res.flatten()
	h = __prepend(X).dot(theta1.transpose())
	h = __prepend(sigmoid(h)).dot(theta2.transpose())
	h = sigmoid(h).flatten()
	J = - (res.transpose().dot(np.log(h)) + (-res + 1).transpose().dot(np.log(-h + 1))) / m
	J += np.sum(np.power(theta1[:, 1:].flatten(), 2)) * lambd / (2 * m)
	J += np.sum(np.power(theta2[:, 1:].flatten(), 2)) * lambd / (2 * m)

	return J

def gradientFunction(theta1, theta2, X, y, lambd):
	m = X.shape[0]
	num_label = theta2.shape[0]
	theta1_grad = np.zeros(theta1.shape)
	theta2_grad = np.zeros(theta2.shape)
	for l in range(m):
		y_l = np.arange(num_label)[np.newaxis].transpose()
		y_l = (y_l == y[l])
		a_1 = __prepend(X[l:l+1, :]).transpose()
		z_2 = theta1.dot(a_1)
		a_2 = __prepend(sigmoid(z_2), axis = 0)
		z_3 = theta2.dot(a_2)
		a_3 = sigmoid(z_3)
		d_3 = a_3 - y_l
		d_2 = theta2.transpose().dot(d_3) * sigmoidGradient(__prepend(z_2, axis = 0))
		d_2 = d_2[1:]
		theta1_grad = theta1_grad + d_2.dot(a_1.transpose())
		theta2_grad = theta2_grad + d_3.dot(a_2.transpose())

	tmp = np.copy(theta1)
	tmp[:, 0:1] = np.zeros((theta1.shape[0], 1))
	theta1_grad = (theta1_grad + tmp*lambd) / m
	tmp = np.copy(theta2)
	tmp[:, 0:1] = np.zeros((theta2.shape[0], 1))
	theta2_grad = (theta2_grad + tmp*lambd) / m

	return flatten(theta1_grad, theta2_grad)

def optimize(theta1, theta2, X, y, lambd):
	x0 = flatten(theta1, theta2)
	def fct(t):
		t1, t2 = reshape(t, (theta1.shape, theta2.shape))
		return costFunction(t1, t2, X, y, lambd)
	def fctprime(t):
		t1, t2 = reshape(t, (theta1.shape, theta2.shape))
		return gradientFunction(t1, t2, X, y, lambd)
	res = fmin_cg(fct, x0, fprime = fctprime, maxiter = 40, norm = 0.01, epsilon = 0.0001, disp = 0)
	return (reshape(res, (theta1.shape, theta2.shape)), fct(res))

def reshape(in_array, sizes):
	length = []
	sum_len = 0
	for i, j in sizes[:-1]:
		sum_len += i*j
		length.append(sum_len)
	last = sizes[-1]
	last = last[0]*last[1]
	if sum_len + last != len(in_array):
		raise ValueError("Sizes don't match")
	splitted = np.split(in_array, length)
	return list(map(lambda arr, size: arr.reshape(size), splitted, sizes))

def flatten(*arrays):
	res = []
	for array in arrays:
		res.append(array.flatten())
	return np.concatenate(res, axis=1)

def sigmoid(z):
	return np.divide(1, np.exp(-z) + 1)

def sigmoidGradient(z):
	g = sigmoid(z)
	return g * (-g + 1)

def randWeights(s_in, s_out):
	eps = 0.12
	return np.random.random((s_out, s_in + 1)) * 2 * eps - eps

def predict(theta1, theta2, X):
	m = X.shape[0]
	num_label = theta2.shape[0]
	h = sigmoid(__prepend(X).dot(theta1.transpose()))
	h = sigmoid(__prepend(h).dot(theta2.transpose()))
	max_values = np.amax(h, axis = 1, keepdims = True)
	max_index = np.argmax(h, axis = 1)[np.newaxis].transpose()
	return (max_index, max_values)

def display(mat):
	import matplotlib.pyplot as plt
	import matplotlib.cm as cm
	height, width = 50, 50 #in pixels
	spines = 'left', 'right', 'top', 'bottom'

	labels = ['label' + spine for spine in spines]

	tick_params = {spine : False for spine in spines}
	tick_params.update({label : False for label in labels})

	img = - mat
	max_val = np.amax(np.abs(img))/2
	img = img / max_val / 2 + max_val
	img *= 255

	desired_width = 8 #in inches
	scale = desired_width / float(width)

	fig, ax = plt.subplots(1, 1, figsize=(desired_width, height*scale))
	img = ax.imshow(img, cmap=cm.Greys_r, interpolation='none')

	#remove spines
	for spine in spines:
	    ax.spines[spine].set_visible(False)

	#hide ticks and labels
	ax.tick_params(**tick_params)

	#preview
	plt.show()






data = loadmat('handwrittings.mat')

perm = np.random.permutation(data['X'].shape[0])
tmp_X = np.zeros(data['X'].shape)
tmp_y = np.zeros(data['y'].shape)
for i in range(len(perm)):
	tmp_X[perm[i], :] = data['X'][i, :]
	tmp_y[perm[i], :] = data['y'][i, :]

X = tmp_X[:3500, :]
X_test = tmp_X[3500:, :]

#with open("res_values", "w") as f:
#	np.set_printoptions(threshold = np.nan)
#	print(X[0,:], file=f)
#	display(reshape(X[0,:], ((20, 20),))[0])
#	exit()
y = tmp_y[:3500, :]
y_test = tmp_y[3500:, :]

y = np.fromiter((value % 10 for value in y), dtype = np.float, count = len(y))[np.newaxis].transpose() # values from 1 to 10 because of octave (need to process it so 10 => 0)
y_test = np.fromiter((value % 10 for value in y_test), dtype = np.float, count = len(y_test))[np.newaxis].transpose() # values from 1 to 10 because of octave (need to process it so 10 => 0)

mid_layer = 25
lambd = 1

theta1_0 = randWeights(400, mid_layer)
theta2_0 = randWeights(mid_layer, 10)

res = optimize(theta1_0, theta2_0, X, y, lambd)
t1 = res[0][0]
t2 = res[0][1]

#np.set_printoptions(threshold = np.nan)
#with open("theta1", "w") as f:
#	print(t1, file=f)
#with open("theta2", "w") as f:
#	print(t2, file=f)

#p = predict(t1, t2, X)

#with open("res_values", "w") as f:
np.set_printoptions(threshold = np.nan)
#	print(p[1], file=f)
#v = (y == p[0])
#for i in range(len(v)):
#	if not v[i]:
#		display(reshape(X[i,:], ((20, 20),))[0])
#print(np.mean(y == (p[0]))*100)
thetas = {}
thetas["theta1"] = t1.tolist()
thetas["theta2"] = t2.tolist()

p = predict(t1, t2, X)
print(np.mean(y == (p[0]))*100)
p = predict(t1, t2, X_test)
print(p[0].shape)
print(np.mean(y_test == (p[0]))*100)


exit()
app = Flask(__name__)

@app.route("/check")
def hello():
	return "Hello"

@app.route("/")
def getThetas():
	try:
		return json.dumps(thetas)
	except Exception as e:
		return str(e)


app.run(host='0.0.0.0')
