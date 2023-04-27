import numpy as np

class Perceptron(object):
	def __init__(self, eta=0.01, n_iter=50, random_state=1):
		self.eta = eta #learning rate
		self.n_iter = n_iter
		self.random_state = random_state #seed for random num generation. to repeat experiments.

	def fit(self, X, y):
		#Function to fit the Training Data, the perceptron algorithm.

		#X is array with shape [num_of_examples, num_of_features] with training data.
		#y is array with shape [num_of_examples] with target values.
		rgen = np.random.RandomState(self.random_state)

		#initially define our weights with small, random normally distributed data corresponding to the 
		#dimensions in X. will scale with higher dimensions because of that shape function.
		self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
		self.errors_ = []

		#Algorithm runs n_iter times.
		for _ in range(self.n_iter):
			errors = 0
			for xi, target in zip(X, y):
				#update our coefficient for each example based on our learning rate and 
				#the difference between the prediction and the value.
				#once the prediction is correct, the coefficient doesn't change.
				update = self.eta * (target - self.predict(xi))
				self.w_[1:] += update * xi
				self.w_[0] += update
				errors += int(update != 0.0)
			#in each iteration, add the number of misclassifications to the error array.
			#useful for tracking the learning.
			self.errors_.append(errors)
		return self

	def net_input(self, X):
		#Calculate the Net Input
		#Dot the set of coefficients for the data point and the set of values for the data point.
		return np.dot(X, self.w_[1:] + self.w_[0])

	def predict(self, X):
		#Return class label after unit step
		#if the coefficients predict the correct label for the data point return 1, else -1
		return np.where(self.net_input(X) >= 0.0, 1, -1)

