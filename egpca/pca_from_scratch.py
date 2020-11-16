import numpy as np

np.random.seed(123)



def de_mean_matrix(A: np.ndarray) -> np.ndarray:
    return A - A.mean(axis=0, keepdims=True)


A = np.array([[1, 2, 3], [3, 4, 5]])

print(A)
np.testing.assert_array_equal(de_mean_matrix(A), np.array([[-1, -1, -1.], [ 1,  1,  1.]]))