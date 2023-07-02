import numpy as np

matrix = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
vector = np.array([2, 3, 4, 5, 6])

result = np.multiply(matrix, vector[:, np.newaxis])

print(result)

# import numpy as np
# A = np.array([[1, 2, 3, 4]])
# B = np.array([[5, 6, 7, 8], [5, 6, 7, 8]])

# # Vertical (row-wise) stacking
# C = np.concatenate((A, B), axis=0)


# # import numpy as np
# # x = np.array([1,2,3])
# # print(f"x = {x}")

# # tmp = np.max(x)
# # print(f"tmp = {tmp}")
# # x -= tmp
# # print(f"x = {x}")
# # x = np.exp(x)
# # tmp = np.sum(x)
# # x /= tmp

# import numpy as np

# # Create a 2D array
# x = np.array([[1, 2], [3, 4], [5, 6]])

# # Create a list of row indices
# row_indices = [0, 2]

# # Get the corresponding rows in the 2D array
# result = x[row_indices]

# print(result)