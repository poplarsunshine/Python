import numpy as np
# 布尔索引
X = np.arange(25).reshape(5, 5)
x = X[X > 10]
x = X[(17 > X) & (X > 10)]
print(x)

# sort
# np.sort()
# ndarray.sort()
X = np.random.randint(1, 11, size=(5, 5))
print(X)
print("X with sorted columns :\n", np.sort(X, axis = 0))
print("X with sorted rows :\n", np.sort(X, axis = 1))
