import numpy as np

# basic list, would double list size not use arithmetic
my_list = [1, 2, 3, 4]
print(my_list)
my_list = my_list * 2
print(my_list)

# numpy array, uses arithemtic
array = np.array([1, 2, 3, 4])
print(array)
array = array * 2
print(array)
