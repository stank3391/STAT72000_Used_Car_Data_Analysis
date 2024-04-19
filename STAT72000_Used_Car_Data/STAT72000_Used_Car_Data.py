import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px
from plotly.subplots import make_subplots
from scipy import stats
import os

warnings.filterwarnings('ignore')
sns.set_theme(style="darkgrid")

try:
    data = pd.read_csv("../DataSet/Car details v3.csv")
except:
    data = pd.read_csv("./DataSet/Car details v3.csv")

data.describe()
data.head()

data.isnull().sum()
data = data.dropna(axis=0)

def convertToNumber(s:str):
    d = ""
    for i in list(s):
        if i.isdigit():
            d += i
    return eval(d)

data["mileage"] = data["mileage"].apply(convertToNumber)
data["engine"] = data["engine"].apply(convertToNumber)
data["max_power"] = data["max_power"].apply(convertToNumber)

data.head()
data.isnull().sum()
data = data.drop(['torque','name','owner'],axis=1) #drop unused data
data.head()
data['transmission'] = data['transmission'].replace({'Automatic': 1, 'Manual': 0}) #convert string to number
data.head()
data['seller_type'] = data['seller_type'].replace({'Trustmark Dealer' : 2, 'Individual': 1, 'Dealer': 0}) #convert string to number
data.head()
data['fuel'] = data['fuel'].replace({'LPG': 3, 'CNG': 2, 'Diesel': 1, 'Petrol': 0}) #convert string to number
data.head()
    
dfs = [data[[col, 'selling_price']] for col in data]
out = []
for x in dfs:
    out.append(x[(np.abs(stats.zscore(x)) < 3).all(axis=1)])
dfs = out

for col in dfs:
    print("Mean: ")
    print(col.mean());
    print("\nMedian: ")
    print(col.median());
    print("\nMax: ")
    print(col.max());
    print("\nMin: ")
    print(col.min());
    print("\nStandard Deviation: ")
    print(col.std());
    print("\nCount: ")
    print(col.count());
    print("\nCorrelation: ")
    print(col.corr())
    print("\n\n\n")

for col in dfs:
    sns.scatterplot(data=col, x=col.iloc[:,0], y=col.iloc[:,1])
    plt.title(f"Scatter Plot between {col.columns[0]} and {col.columns[1]}.")
    plt.show()

for col in dfs:
    count = col.iloc[:,0].value_counts()
    plt.pie(count, labels=count.index, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.1)    
    plt.title(f"Distribution of {col.columns[0]} by Percentage.")
    plt.show()

for col in dfs:
    sns.histplot(data=col, x=col.iloc[:,0])
    plt.title(f"Distribution of Vehicles by {col.columns[0]}.")
    plt.show()


