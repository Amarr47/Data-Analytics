import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
headers=["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df = pd.read_csv('cars.csv',names=headers)
df['normalized-losses'].replace("?",np.nan,inplace=True)
df['normalized-losses']=df['normalized-losses'].astype('float')
avgmean = df['normalized-losses'].mean(axis=0)
df['normalized-losses'].replace(np.nan,avgmean,inplace=True)
df['bore'].replace("?",np.nan,inplace=True)
df['bore']=df['bore'].astype('float')
avgb = df['bore'].mean(axis=0)
df['bore'].replace(np.nan,avgb,inplace=True)
df['stroke'].replace("?",np.nan,inplace=True)
df['stroke']=df['stroke'].astype('float')
avgs = df['stroke'].mean(axis=0)
df['stroke'].replace(np.nan,avgs,inplace=True)
df['horsepower'].replace("?",np.nan,inplace=True)
df['horsepower']=df['horsepower'].astype('float')
avghp = df['horsepower'].mean(axis=0)
df['horsepower'].replace(np.nan,avghp,inplace=True)
df['peak-rpm'].replace("?",np.nan,inplace=True)
df['peak-rpm']=df['peak-rpm'].astype('float')
avgpr = df['peak-rpm'].mean(axis=0)
df['peak-rpm'].replace(np.nan,avgpr,inplace=True)
df['price'].replace("?",np.nan,inplace=True)
df['price']=df['price'].astype('float')
avgp = df['price'].mean(axis=0)
df['price'].replace(np.nan,avgp,inplace=True)
bins = np.linspace(min(df['price']),max(df['price']),4)
group =['low','medium','high']
df['Range of cost'] = pd.cut(df['price'],bins,labels=group)
plt.bar(group,df["Range of cost"].value_counts())
dummy = pd.get_dummies(df['fuel-type'])
dummy.rename(columns={'diesel':'Fuel type-Diesel','gas':'Fuel type-Gas'},inplace=True)
df = pd.concat([df,dummy],axis=1)
df.drop('fuel-type',axis=True,inplace=True)
print(df.head())
df.to_csv('Cleandata1.csv')