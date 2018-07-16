import pandas as pd

items = {"Alice" : pd.Series(data = [23, 34, 232, 20], index = ["bike", "desk", "book", "knife"]),
        "Bob" : pd.Series(data = [300, 499, 22], index = ["pen", "desk", "eggs"])}

print("items=\n", items)

dataF = pd.DataFrame(items)
print("DataFrame=\n", dataF)
print('dataF has shape:', dataF.shape)
print('dataF has dimension:', dataF.ndim)
print('dataF has a total of:', dataF.size, 'elements')
print('The data in dataF is:\n', dataF.values)
print('The row index in dataF is:\n', dataF.index)
print('The column index in dataF is:\n', dataF.columns)

# 部分导入
dataF = pd.DataFrame(items, index = ["book"], columns = ["Alice"])
print("DataFrame=\n", dataF)

# 其他创建方式
# 1、列表字典
# 字典的值为列表 index 默认数字索引，字典中的所有列表（数组）长度必须一致，否则报错
data = {'Integers' : [1,2,4],
        'Floats' : [4.5, 8.2, 9.6]}
df = pd.DataFrame(data)
print("df=\n", df)
df = pd.DataFrame(data, index = ['label 1', 'label 2', 'label 3'])
print("index df=\n", df)

# 2、字典列表
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]
store_items = pd.DataFrame(items2, index = ["lb1", "lb2"])
print("store_items=\n", store_items)

### 访问DataFrame中的元素
# dataframe[column][row]
print("store_items=\n", store_items[["bikes", "watches"]])
print("store_items=\n", store_items["watches"]["lb1"])
# 添加
store_items["new"] = [44, 44]
print("new store_items=\n", store_items)
store_items["sum"] = store_items["bikes"] + store_items["watches"]
print("new store_items=\n", store_items)

new_item = [{'glasses': 20, 'pants': 30, 'watches': 5}]
new_store = pd.DataFrame(new_item, index = ["lb3"])
store_items = store_items.append(new_store)
print("new store_items=\n", store_items)

store_items['new watches'] = store_items['watches'][1:]
print("new store_items=\n", store_items)

# insert
# dataframe.insert(loc,label,data) 方法
# 使我们能够将新列（具有给定列标签和给定数据）插入 dataframe 的 loc 位置
store_items.insert(4, 'shoes', [8,5,0])
print("store_items=\n", store_items)

# 删除
# 要删除 DataFrame 中的行和列，我们将使用 .pop() 和 .drop() 方法。
# .pop() 方法仅允许我们删除列
# 而 .drop() 方法可以同时用于删除行和列，只需使用关键字 axis 即可
store_items.pop('new watches')
print("store_items=\n", store_items)
print("drop store_items=\n", store_items.drop(['lb2'], axis = 0))

# 改名
# .rename()
store_items = store_items.rename(columns = {'bikes': 'hats'})
print("rename store_items=\n", store_items)
store_items = store_items.rename(index = {'lb1': 'label1'})
print("rename store_items=\n", store_items)
# 将某列设置为索引
store_items = store_items.set_index('pants')
print("reindex store_items=\n", store_items)

### NaN
print("isnull sum sum=", store_items.isnull().sum().sum())
print("isnull count count=", store_items.isnull().count().count())
# dropna
# print("store_items dropna=\n", store_items.dropna(axis = 0))
# print("store_items dropna=\n", store_items.dropna(axis = 1))

# fillna()
print("fillna store_items=\n", store_items.fillna(0))
# .fillna() 方法将 NaN 值替换为 DataFrame 中的上个值，称之为前向填充。
# 在通过前向填充替换 NaN 值时，我们可以使用列或行中的上个值。
# .fillna(method = 'ffill', axis) 将通过前向填充 (ffill) 方法沿着给定 axis 使用上个已知值替换 NaN 值
print("fillna store_items=\n", store_items.fillna(method = 'ffill', axis = 0))
# .fillna(method = 'backfill', axis) 将通过后向填充 (backfill) 方法沿着给定 axis 使用下个已知值替换 NaN 值
print("fillna store_items=\n", store_items.fillna(method = 'backfill', axis = 1))

# .interpolate(method = 'linear', axis) 线性平均值
