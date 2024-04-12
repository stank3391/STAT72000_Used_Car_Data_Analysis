############Imports#####################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px
from plotly.subplots import make_subplots
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
data = data.drop(['seller_type','torque','name','owner'],axis=1)
data.head()
data.fuel.unique()
data_new = pd.get_dummies(data=data, columns=['fuel'], drop_first=True, dtype=int)
data_new.head()
data_new['transmission'] = data_new['transmission'].replace({'Automatic': 1, 'Manual': 0})
data_new.head()
#data_new['fuel'] = data_new['fuel'].replace({'fuel_Diesel': 2, 'fuel_LPG': 1, 'fuel_Petrol': 0})
#data_new.head()

from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
mmScaler = MinMaxScaler()
mmScaler_y = MinMaxScaler()

label_enc = LabelEncoder()

x = data_new[['year', 'km_driven','transmission', 'mileage', 'engine', 'max_power', 'seats', 'fuel_Diesel', 'fuel_LPG', 'fuel_Petrol']].values
y = data_new[['selling_price']].values
x[:,0] = label_enc.fit_transform(x[:,0])
x = mmScaler.fit_transform(x)
y = mmScaler_y.fit_transform(y)



#############DATA ANALYSIS####################
# import plotly.graph_objects as go
# correlation_matrix = data_new.corr()

# corr = go.Heatmap(
#     z = correlation_matrix.values,
#     x = correlation_matrix.columns,
#     y = correlation_matrix.columns,
#     colorscale='RdYlBu',
#     colorbar=dict(title='Correlation')
# )

# layout = go.Layout(
#     title='Heatmap of Correlation',
#         xaxis=dict(title='Columns'),
#     yaxis=dict(title='Columns'),
#     height= 800
# )

# fig = go.Figure(data=corr, layout=layout)
# fig.show()
# correlations = data_new.corrwith(data_new['selling_price'])
# correlations
# for column in data_new.columns:
#     sns.scatterplot(data=data_new, x=column, y='selling_price')
#     plt.title(f"Scatter Plot between {column} and selling_price")
#     plt.show()



# #Seats vs Selling Price
# sns.scatterplot(data=data_new, x='seats', y='selling_price')
# plt.title(f"Seats vs Selling Price")
# plt.show()

# #Seats Count
# sns.countplot(data=data_new, x='seats')
# plt.title(f"Seats vs Selling Price")
# plt.show()

# #Seats Histogram
# sns.histplot(data=data_new, x='seats')
# plt.title(f"Number of Seats in Cars")
# plt.show()

# #Seats Bar
# sns.barplot(data=data_new, x='seats', y='selling_price')
# plt.title(f"Seats vs Selling Price")
# plt.show()

df = pd.DataFrame(data_new);
# print(" -- Seats -- ")
# print("Mean: ")
# print(df['seats'].mean());
# print("Median: ")
# print(df['seats'].median());
# print("Max: ")
# print(df['seats'].max());
# print("Min: ")
# print(df['seats'].min());
# print("Standard Deviation: ")
# print(df['seats'].std());
# print("Count: ")
# print(df['seats'].count());



print(" -- Fuel Type -- ")

diesel = df['fuel_Diesel']
lpg = df['fuel_LPG']
petrol = df['fuel_Petrol']

dcount = diesel.value_counts()[1]
lcount = lpg.value_counts()[1]
pcount = petrol.value_counts()[1]



# declaring data 
data = [dcount, lcount, pcount] 
keys = ['Diesel', 'LPG', 'Petrol'] 
palette_color = sns.color_palette('bright') 
plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%') 
plt.show() 

print("finished?")

#frames = [diesel, lpg, petrol]

#fuel = pd.concat(frames)


#print(fuel)

# print("Median: ")
# print(fuel.median());
# print("Max: ")
# print(fuel.max());
# print("Min: ")
# print(fuel.min());
# print("Standard Deviation: ")
# print(fuel.std());
# print("Count: ")
# print(fuel.count());


# df.groupby(['fuel_Diesel']).sum().plot(kind='pie', y=fuel.values)