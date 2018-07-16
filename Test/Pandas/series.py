import pandas as pd

groceries = pd.Series(data = [30, 6, "Yes", "No"], index = ["eggs", "apples", "milk", "bread"])

print("groceries=\n", groceries)
print('Groceries has shape:', groceries.shape)
print('Groceries has dimension:', groceries.ndim)
print('Groceries has a total of', groceries.size, 'elements')

print('The data in Groceries is:', groceries.values)
print('The index of Groceries is:', groceries.index)

# 如果你处理的是非常庞大的 Pandas Series，
# 并且不清楚是否存在某个索引标签，可以使用 in 命令检查index是否存在该标签：
x = 'bananas' in groceries
y = 'bread' in groceries
print('Is bananas an index label in Groceries:', x)
print('Is bread an index label in Groceries:', y)

# 为了清晰地表明我们指代的是索引标签还是数字索引，
# Pandas Series 提供了两个属性 .loc 和 .iloc，帮助我们清晰地表明指代哪种情况。
# 属性 .loc 表示位置，用于明确表明我们使用的是标签索引。
# 属性 .iloc 表示整型位置，用于明确表明我们使用的是数字索引。
print('groceries:', groceries["eggs"])
print('groceries:\n', groceries[["eggs"]])
print('groceries:\n', groceries[[0, 1]])
print('groceries:\n', groceries.loc[["eggs", "apples"]])
print('groceries:\n', groceries.iloc[[0, 1]])

# .drop() 方法删除 Pandas Series 中的条目
# 关键字 inplace 设为 True，原地地从 Pandas Series 中删除条目
print('Original Grocery List:\n', groceries)
print('We remove apples (out of place):\n', groceries.drop('apples'))
print('Grocery List after removing apples out of place:\n', groceries)

print('Original Grocery List:\n', groceries)
print('We remove apples (out of place):\n', groceries.drop('apples', inplace=True))
print('Grocery List after removing apples out of place:\n', groceries)
