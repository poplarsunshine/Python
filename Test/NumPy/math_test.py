import numpy as np

# add subtract multiply divide
x = np.array([1, 2, 3, 4])
y = np.array([5.5, 6.5, 7.5, 8.5])

print("%20s %s" % ("x + y = ", (x + y)))
print("%20s %s" % ("add(x, y) = ", np.add(x, y)))

print("%20s %s" % ("x - y = ", (x - y)))
print("%20s %s" % ("subtract(x, y) = ", np.subtract(x, y)))

print("%20s %s" % ("x * y = ", (x * y)))
print("%20s %s" % ("multiply(x, y) = ", np.multiply(x, y)))

print("%20s %s" % ("x / y = ", (x / y)))
print("%20s %s" % ("divide(x, y) = ", np.divide(x, y)))
