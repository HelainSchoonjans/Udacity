"""Softmax."""

scores = [30.0, 10.0, 2.0]

import numpy as np
import math

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    # softmax function: S(y_i) = e^(y_i) / e^ (Sum_j y_j)
    #exponents = np.vectorize(lambda arr: math.exp(arr))(x)
    #sum_exponents = np.sum(exponents)
    #return np.vectorize(lambda arr: arr/sum_exponents)(exponents)
    return np.exp(x) / np.sum(np.exp(x), axis=0)

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()