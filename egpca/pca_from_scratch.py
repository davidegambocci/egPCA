import numpy as np
from typing import List


np.random.seed(123)

#
def de_mean_matrix(A: np.ndarray) -> np.ndarray:
    """returns the result of subtracting from every value in A the mean
    value of its column. the resulting matrix has mean 0 in every column"""
    return A - A.mean(axis=0, keepdims=True)


#
def direction(w: List[float]) -> List[float]:
    mag = sum([w_i ** 2 for w_i in w])
    return [w_i / mag for w_i in w]


#
def directional_variance_i(x_i, w):
    """the variance of the row x_i in the direction determined by w"""
    return

#
np.testing.assert_array_equal(de_mean_matrix(np.array([[1, 2, 3], [3, 4, 5]])), np.array([[-1, -1, -1.], [ 1,  1,  1.]]))