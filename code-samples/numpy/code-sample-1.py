import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Perform mathematical operations on arrays
arr_squared = arr ** 2
print(arr_squared)

# Perform element-wise operations between arrays
arr2 = np.array([2, 4, 6, 8, 10])
arr_sum = arr + arr2
print(arr_sum)

# Perform array slicing and indexing
arr_slice = arr[1:4]
print(arr_slice)