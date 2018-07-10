import numpy as np

# 内容为0
X = np.zeros((3, 4))
print(X)

# 内容为1
Y = np.ones((3, 4))
print(Y)

# 内容为制定值
Z = np.full((3, 4), 2)
print(Z)

# 单位矩阵
A = np.eye(5)
print(A)

# 对角矩阵 diag ：对角矩阵是仅在主对角线上有值的方形矩阵
D = np.diag([1, 2, 6, 4])
print(D)

# arange : 给定区间内值均匀分布的 ndarray
# 当传入一个参数时：0到N-1的连续整数
x = np.arange(10)
print(x)
# 当传入二个参数时：np.arange(start,stop),start到stop-1的连续整数
x = np.arange(4, 8)
print(x)
# 当传入三个参数时: np.arange(start,stop,step),step 为相邻值的差
x = np.arange(4, 8, 2)
print(x)

# np.linspace(start, stop, N) 函数返回 N 个在闭区间 [start, stop] 内均匀分布的数字
# 默认包含闭区间 np.linspace(0,25,10, endpoint = False)
x11 = np.linspace(0, 25, 11)
x10 = np.linspace(0, 25, 10, endpoint = False)
print(x11, "\n", x10)

# reshape np.reshape(ndarray, new_shape) 函数会将给定 ndarray 转换为指定的 new_shape
x = np.arange(24)
print("reshape:\n", x)
x = np.reshape(x, (4, 6))
print("reshape:\n", x)
x = np.reshape(x, (2, 3, 4))
print("reshape:\n", x)
# 点记法(.) NumPy 的一大特性是某些函数还可以当做方法使用
x = np.arange(20).reshape((4, 5))
print("arange.reshape:\n", x)

# 随机
# np.random.random(shape) 函数创建具有给定形状的 ndarray，其中包含位于半开区间 [0.0, 1.0) 内的随机浮点数
x = np.random.random((4, 5))
print(x)
# np.random.randint(start, stop, size = shape) 会创建一个具有给定形状的 ndarray，其中包含在半开区间 [start, stop) 内的随机整数
x = np.random.randint(4, 9, (4, 5))
print(x)
# np.random.normal(mean, standard deviation, size=shape) 会创建一个具有给定形状的 ndarray，
#其中包含从正态高斯分布（具有给定均值mean和标准差standard deviation）中抽样的随机数字
R = np.random.normal(0, 0.1, size=(1000,1000))
print(R)
