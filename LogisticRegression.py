"""

Logistic Regression Object that can be used in futures ML projects !

Prediction function = sigmoid( W.T * x + B)
So for each W (feature), we have a probability (0 to 1) that a fact is true or false.
In order to optimize our parameters (W and B) we have to perfom a gradient descent algorithm.
For that we use an error function specifically called in this case : Binary Coss-Entropy Loss AKA Cost function.
The partial derivatives of this Cost Function with respect to W and B will give use the direction
in order to decrease the value of the Cost like so (just like in linear regression) :

dw = (1 / n_samples) * X.T * (Ypred — y)
db = (1 / n_samples) * (Ypred — y)

n_samples = the number of samples (rows in training data)
Ypred = the prediction function

And so we can update our parameters :

W = W - L * dW
B = B - L * dB

L is the learning rate -> Used in the Gradient Ascent Algorithm
Epoch is the machine learning term for 'Iteration'
W is the array of Weight of the length of the number of features in X
B is the bias (the second parameter of the prediction formula)

"""

import numpy as np
import math

class LogisticRegression:

    def __init__(self, L=0.001, epochs=1000):
        self.L = L
        self.epochs = epochs
        self.W = None
        self.B = 0

    def train(self, X, y):
        # Get the shape of X
        n_samples, n_features = X.shape
        
        # Init parameters weight and b to zeros
        self.W = np.zeros((n_features, 1))
        self.B = 0
        
        # Make the real values n_samples * 1
        y = y.reshape(n_samples, 1)
                
        for epoch in range(self.epochs):
            # Compute prediction with our actual weights and bias
            linear_prediction = np.dot(X, self.W) + self.B
            
            # Apply sigmoid function to our prediction, this will give us a probability (0 - 1)
            prediction_proba = self.sigmoid(linear_prediction)
            
            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (prediction_proba - y))
            db = (1 / n_samples) * np.sum((prediction_proba - y))

            # Update parameters
            self.W -= self.L * dw
            self.B -= self.L * db
        
        return self.W, self.B, prediction_proba

    def classificate(self, predictions):
        return [1 if predictions[i] > 0.5 else 0 for i in range(len(predictions))];


    def sigmoid(self, x):
        return (1.0 / (1.0 + np.exp(-x)))
    
    
def ft_mean(values):
    mean = 0
    n = len(values)
    for i in range(len(values)):
        if values[i] != values[i]:
            n -= 1
        else:
            mean += values[i]
    return mean / n

def standard_deviation(values):
    mean = ft_mean(values)
    sum = 0
    for row in range(len(values)):
        if values[row] != values[row]:
            sum += 0
        else:
            sum += (values[row] - mean) ** 2
    return math.sqrt(sum / len(values))

def standardize(X):
    n_samples, n_features = X.shape
    for i in range(n_features):
        mean = ft_mean(X.iloc[:,i])
        std  = standard_deviation(X.iloc[:,i])
        for j in range(len(X.iloc[:,i])):
            if X.iloc[j,i] != X.iloc[j,i]:
                X.iloc[j,i] = 0
            else:
                X.iloc[j,i] = (X.iloc[j,i] - mean) / std
    return X