############Imports#####################
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


############PREPROCESSING#################
try:
    print("original path")
    data = pd.read_csv("../DataSet/Car details v3.csv")
except:
    print("works on my machine path")
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

#### ACTUAL CODE HEREEEEEEE REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

#problem is shared database, create new dataframe per data column
#create a data frame for each column and populate that dataframe with the trimmed data
#put the trimmed data frame into the dataframes dict
dataframes = []
for column in data.columns:
    df = pd.DataFrame(data[column])
    q_low = df[column].quantile(0.05)
    q_hi  = df[column].quantile(0.95)
    dataframes.append(df[(df[column] < q_hi) & (df[column] > q_low)])
    

for column in data.columns:
    df = pd.DataFrame(data[column])

    print(column + "\n")
    print("Mean: ")
    print(df[column].mean());
    print("Median: ")
    print(df[column].median());
    print("Max: ")
    print(df[column].max());
    print("Min: ")
    print(df[column].min());
    print("Standard Deviation: ")
    print(df[column].std());
    print("Count: ")
    print(df[column].count());
    print("Correlation: ")
    print(df[column].corr(df['selling_price']))
    print("\n\n\n")

for column in data.columns:
    df = pd.DataFrame(data)
    # q_low = df[column].quantile(0.05)
    # q_hi  = df[column].quantile(0.95)
    # df = df[(df[column] < q_hi) & (df[column] > q_low)]
    sns.scatterplot(data=df, x=column, y='selling_price')
    plt.title(f"Scatter Plot between {column} and selling_price")
    plt.show()

for column in data.columns:
    df = pd.DataFrame(data)
    # q_low = df[column].quantile(0.05)
    # q_hi  = df[column].quantile(0.95)
    # df = df[(df[column] < q_hi) & (df[column] > q_low)]
    testValues = df[column].value_counts()
    plt.pie(testValues, labels=testValues.index, autopct='%1.0f%%', pctdistance=0.8, labeldistance=1.1)    
    plt.title(f"Distribution of {column} by count.")
    #plt.legend()
    plt.show()

for column in data.columns:
    df = pd.DataFrame(data)
    # q_low = df[column].quantile(0.05)
    # q_hi  = df[column].quantile(0.95)
    # df = df[(df[column] < q_hi) & (df[column] > q_low)]
    sns.histplot(data=df, x=column)
    plt.title(f"Distribution of {column}")
    plt.show()

