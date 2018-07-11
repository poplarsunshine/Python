import numpy as np

# add subtract multiply divide
x = np.array([1, 2, 3, 4])
y = np.array([5.5, 6.5, 7.5, 8.5])
print("x=", x)

# 应用数学
print("%20s %s" % ("x + y = ", (x + y)))
print("%20s %s" % ("add(x, y) = ", np.add(x, y)))

print("%20s %s" % ("x - y = ", (x - y)))
print("%20s %s" % ("subtract(x, y) = ", np.subtract(x, y)))

print("%20s %s" % ("x * y = ", (x * y)))
print("%20s %s" % ("multiply(x, y) = ", np.multiply(x, y)))

print("%20s %s" % ("x / y = ", (x / y)))
print("%20s %s" % ("divide(x, y) = ", np.divide(x, y)))

print("科学计数 EXP(x) = ", np.exp(x))
print("开平方 SQRT(x) = ", np.sqrt(x))
print("次方 POW(x, 3) = ", np.power(x, 3))

# 统计学
X = np.arange(1, 5).reshape(2, 2)
print("X=\n", X)
# 平均值 mean
print("mean=\n", X.mean())
print("cols mean=\n", X.mean(axis=0))
print("rows mean=\n", X.mean(axis=1))
# 和 sum
print("sum=\n", X.sum())
print("cols sum=\n", X.sum(axis=0))
print("rows sum=\n", X.sum(axis=1))
# 标准差 std
print("std=\n", X.std())
print("cols std=\n", X.std(axis=0))
print("rows std=\n", X.std(axis=1))
# 中位数 median
X = np.array([[1, 3, 4], [1, 4, 3], [4, 9, 9]])
print("median=\n", np.median(X))
print("cols median=\n", np.median(X, axis=0))
print("rows median=\n", np.median(X, axis=1))
# 最值 max min
print("max=\n", np.max(X))
print("cols max=\n", np.max(X, axis=0))
print("rows max=\n", np.max(X, axis=1))
