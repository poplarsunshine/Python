import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.DataFrame(data = [{"cat_var" : 20}, {"cat_var" : 25}, {"cat_var" : 29}, {"cat_var" : 14}])
print(df)

sb.countplot(data = df, x = "cat_var")
