import numpy as np

# delete
# np.delete(ndarray, elements, axis)
# 此函数会沿着指定的轴从给定 ndarray 中删除给定的元素列表
Y = np.arange(9).reshape((3, 3))
print(Y)
w = np.delete(Y, 0, axis=0)
v = np.delete(Y, [0], axis=0)
print("w:", w)
print("v:", v)

# append
# np.append(ndarray, elements, axis)
# 该函数会将给定的元素列表沿着指定的轴附加到 ndarray 中
x = np.array([1, 2, 3, 4, 5])
y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
w = np.append(y, [[10, 11, 12]], axis=0)
v = np.append(y, [[10], [11], [12]], axis=1)
print("w:", w)
print("v:", v)

# insert
# np.insert(ndarray, index, elements, axis)
# 此函数会将给定的元素列表沿着指定的轴插入到 ndarray 中，并放在给定的索引前面
i = np.insert(y, 1, 12, axis=0)
print("i:", i)

# 堆叠 np.vstack((array1, array2)) 纵向，hstack横向
s = np.vstack((y, [10, 11, 12]))
print("s:", s)
