import numpy as np

# zero dimsional array
array_1 = np.array(1)
print(array_1, array_1.ndim, array_1.shape)

# one dimensional array
array_2 = np.array([1, 2, 3])
print(array_2, array_2.ndim, array_2.shape)

# two dimensional array
array_3 = np.array([[1, 2, 3]])
print(array_3, array_3.ndim, array_3.shape)

# array accessing
print(array_3[0, 1])
