import numpy as np 

"""

Idea behind softmax activation function:

input -> exponentiation -> normalization -> output

exponentiation: raises all input values to the power of e
it solves the problem of negative inputs 

normalization: it divides the exponentiated values by their sum of all the exponentiated values
it ensures that the output values sum to 1, forming a valid probability distribution


"""
class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities
