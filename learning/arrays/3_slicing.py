import numpy as np

# subscript slicing
array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(array1[0:4:2])
print(array1[2:, 2:])
