import numpy as np

# 切片
X = np.arange(20).reshape(4, 5)
print(X)

Z = X[1:4, 2:5]
print(Z)

v1 = X[2, :]
print("一维的:\n", v1)

v2 = X[2:3, :]
print("二维的:\n", v2)

# copy
# np.copy(ndarray) 函数会创建给定 ndarray 的一个副本
C1 = np.copy(X[1:4, 2:5])
C2 = X[1:4, 2:5].copy()
print(C1)
print(C2)

# 提取对角线元素
# np.diag(ndarray, k=N) 函数会以 N 定义的对角线提取元素。
# 默认情况下，k=0，表示主对角线。
# k > 0 的值用于选择在主对角线之上的对角线中的元素，
# k < 0 的值用于选择在主对角线之下的对角线中的元素
X = np.arange(16).reshape(4, 4)
print("X=\n", X)
print("diag=", np.diag(X))
print("k=1 diag=", np.diag(X, k=1))
print("k=2 diag=", np.diag(X, k=2))
print("k=-1 diag=", np.diag(X, k=-1))

# 提取唯一元素
# np.unique(ndarray) 函数会返回给定 ndarray 中的 唯一元素
X = np.array([[1,2,3],[5,2,8],[1,2,3]])
U = np.unique(X)
print("U=", U)
