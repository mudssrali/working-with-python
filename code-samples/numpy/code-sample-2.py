import numpy as np

# Create a 2D NumPy array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# Perform matrix operations
matrix_transposed = np.transpose(matrix)
print(matrix_transposed)

matrix_sum = matrix + matrix_transposed
print(matrix_sum)

matrix2 = np.array([[1, 2], [3, 5]])

matrix_inverse = np.linalg.inv(matrix2)
print(matrix_inverse)