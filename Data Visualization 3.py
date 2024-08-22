import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from pywaffle import Waffle
df = pd.read_excel('Canada.xlsx',sheet_name='Canada by Citizenship',skiprows=range(20),skipfooter=2)
print(df.head())
print(df.shape)
df.drop(['Type','Coverage','AREA','REG','DEV','Unnamed: 43','Unnamed: 44','Unnamed: 45','Unnamed: 46','Unnamed: 47','Unnamed: 48','Unnamed: 49','Unnamed: 50'],axis=1,inplace=True)
df.rename(columns={'OdName':'Country','AreaName':'Continent','RegName':'Region'},inplace=True)
df['Total'] = df.sum(axis=1)
print(df.head())
years = list(map(str,range(1980,2014)))
#fig = px.sunburst(df,path=['Continent','Country'],values='Total')
#fig = px.pie(df,values='Total',names='Continent')
df.set_index('Country',inplace=True)
df.sort_values(by=['Total'],ascending=False,inplace=True)
print(df.tail())
dfw = df.loc[['San Marino','New Caledonia','Marshall Islands']]
print(dfw)
t = dfw['Total'].sum(axis=0)
prop = dfw.Total/t
print(pd.DataFrame({'Proportion':prop}))
height = 10
width = 40
totalsize = height*width
tiles = (prop*totalsize).round().astype(int)
print(pd.DataFrame({'Tiles':tiles}))
fig=plt.figure(FigureClass=Waffle,rows=10,columns=40,values=tiles,legend={'labels':['San Marino','New Caledonia','Marshall Islands'],'loc':'upper left','bbox_to_anchor':(1,1)})
plt.show()
