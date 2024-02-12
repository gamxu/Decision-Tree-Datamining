import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

col_names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

df = pd.read_csv("irisds\iris.data", header=None, names=col_names)
res = df.describe(percentiles=[.25, .75])
print(res.describe)

sl_mean = res["sepal length"]["mean"]
sw_mean = res["sepal width"]["mean"]
pl_mean = res["petal length"]["mean"]
pw_mean = res["petal width"]["mean"]

sl_std = res["sepal length"]["std"]
sw_std = res["sepal width"]["std"]
pl_std = res["petal length"]["std"]
pw_std = res["petal width"]["std"]

sl_res = []
sw_res = []
pl_res = []
pw_res = []
clas = []

for data in df['sepal length']:    
    # print(data)
    if(data > sl_mean+sl_std):   # more than upper bound
        sl_res.append("sl_higher")
    elif(data < sl_mean-sl_std): # lower than lower bound
        sl_res.append("sl_lower")
    else:                       # in the middle
        sl_res.append("sl_mid")

for data in df['sepal width']:    
    # print(data)
    if(data > sw_mean+sw_std):   # more than upper bound
        sw_res.append("sw_higher")
    elif(data < sw_mean-sw_std): # lower than lower bound
        sw_res.append("sw_lower")
    else:                       # in the middle
        sw_res.append("sw_mid")

for data in df['petal length']:    
    # print(data)
    if(data > pl_mean+pl_std):   # more than upper bound
        pl_res.append("pl_higher")
    elif(data < pl_mean-pl_std): # lower than lower bound
        pl_res.append("pl_lower")
    else:                       # in the middle
        pl_res.append("pl_mid")

for data in df['petal width']:    
    # print(data)
    if(data > pw_mean+pw_std):   # more than upper bound
        pw_res.append("pw_higher")
    elif(data < pw_mean-pw_std): # lower than lower bound
        pw_res.append("pw_lower")
    else:                       # in the middle
        pw_res.append("pw_mid")

for data in df['class']:    
    clas.append(data)

# Create the combined string with formatting
combined_string = ""
for i in range(len(sl_res)):
    data1 = sl_res[i]
    data2 = sw_res[i]
    data3 = pl_res[i]
    data4 = pw_res[i]
    data5 = clas[i]
    combined_string += f"{data1} {data2} {data3} {data4} {data5}\n"

# Open the file in write mode and write the string
with open("irisds\output.txt", "w") as file:
    file.write(combined_string)

print(sl_res)
print(sw_res)
print(pl_res)
print(pw_res)
# print(sl_mean)


# indexes = df.index.to_series()
# df['index'] = indexes

# color_mapping = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}

# fig, ax = plt.subplots(2, 2)
# ax[0, 0].scatter(df['index'], df['sepal length'], s=5, c=df['class'].map(color_mapping))
# ax[0, 1].scatter(df['index'], df['sepal width'], s=5, c=df['class'].map(color_mapping))
# ax[1, 0].scatter(df['index'], df['petal length'], s=5, c=df['class'].map(color_mapping))
# ax[1, 1].scatter(df['index'], df['petal width'], s=5, c=df['class'].map(color_mapping))

# ax[0, 0].set_title('sepal length')
# ax[0, 1].set_title('sepal width')
# ax[1, 0].set_title('petal length')
# ax[1, 1].set_title('petal width')

# plt.show()
