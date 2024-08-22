import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
df = pd.read_csv('Cleandata1.csv')
print(df.corr())
print(df[['engine-size','price']].corr())
d1 = df['engine-location'].value_counts().to_frame()
d1.rename(columns={'engine-location':'number of cars'},inplace=True)
d1.index.name = 'engine-location'
print('\n',d1)
group = df[['body-style','drive-wheels','price']]
gt = group.groupby(['drive-wheels','body-style'],as_index=False).mean()
print('\n',gt)
gpivot = gt.pivot(index='drive-wheels',columns='body-style')
gpivot = gpivot.fillna(0)
print('\n',gpivot)
pcoef,pval = stats.pearsonr(df['engine-size'],~df['engine-size'])
print("The Pearson Correlation Coefficient is", pcoef, "\nwith a P-value of P =", pval)
if(pval<0.001):
    print('Pvalue is Strong')
elif(pval<0.05):
    print('Pvalue is moderate')
elif(pval<0.1):
    print('Pvalue is weak')
else:
    print('No Relationship')
dfcar = df[['engine-size','price']]
fig = plt.figure(figsize=(20,6))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
sns.regplot(x='engine-size',y='price',data=df,ax=ax1)
sns.boxplot(x='body-style', y='price',data=df,ax=ax2)
dfcar.plot(kind='line',ax=ax3)
ax3.set_xlabel('engine-size')
ax3.set_ylabel('price')
plt.pcolor(gpivot,cmap='viridis')
plt.colorbar()
plt.show()