import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
df = pd.read_csv('Cleandata1.csv')
print(df[['horsepower','highway-mpg','engine-size','price']].head(),'\n')
print(df['engine-size'].min(),df['engine-size'].max())
lm = LinearRegression()
A = df[['horsepower']]
B = df['price']
lm.fit(A,B)
print('Predicted Prices are : ' , lm.predict(A.head()))
print('Intercept : ',lm.intercept_,'\n','Coefficent : ',lm.coef_)
print("R Square value is ",lm.score(A,B))
print('MSE is ',mean_squared_error(B,lm.predict(A)),'\n')
C = df[['highway-mpg','engine-size']]
D = df['price']
lm.fit(C,D)
Amar = lm.predict(C)
print('Predicted Prices are : ' , lm.predict(C.head()))
print('Intercept : ',lm.intercept_,'\n','Coefficent : ',lm.coef_)
print("R Square value is ",lm.score(C,D))
print('MSE is ',mean_squared_error(D,lm.predict(C)),'\n')
#sns.regplot(x=df['horsepower'],y=df['price'])
#plt.show()
plt.close()
#sns.residplot(df['highway-mpg'],df['price'])
#plt.show()
plt.close()
#ax1 = sns.distplot(df['price'],hist=False,color='r',label='Actual Value')
#sns.distplot(lm.predict(df[['highway-mpg','engine-size']]),hist=False,color='b',label='Predicted Value',ax=ax1)
plt.xlabel('Price')
plt.ylabel('Proportion of cars')
plt.title('Actual value vs Expected value')
#plt.show()
plt.close()
def polly(model,independent_variable,dependent_variable,name):
    x_new = np.linspace(60,327,205)
    y_new = model(x_new)
    plt.plot(independent_variable,dependent_variable,'.',x_new,y_new,'-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.829,0.829,0.829))
    fig = plt.gcf()
    plt.xlabel(name)
    plt.ylabel('Price of Cars')
    plt.show()
    plt.close()
E = np.polyfit(df['horsepower'],B,3)
F = np.poly1d(E)
print('Cubic Equation: ',F, '\n','Values : ',E)
print(r2_score(D,F(df['horsepower'])))
print(mean_squared_error(D,F(df['horsepower'])))
#polly(F,A,B,'engine-size')
from sklearn.preprocessing import PolynomialFeatures
pr = PolynomialFeatures(degree=2)
print('\n',pr.fit_transform(C.head()))
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
Input=[('scale',StandardScaler()),('polynomial',PolynomialFeatures(include_bias=False)),('model',LinearRegression())]
pipe = Pipeline(Input)
pipe.fit(C,D)
print(pipe.predict(C)[0:6])
new = np.arange(1,100,1).reshape(-1,1)
lm.fit(A,B)
yhit = lm.predict(new)
plt.plot(new,yhit)
fig = plt.figure(figsize=(20,6))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
sns.regplot(x=df['horsepower'],y=df['price'],ax=ax1)
sns.residplot(df['highway-mpg'],df['price'],ax=ax2)
aa = sns.distplot(df['price'],hist=False,color='r',label='Actual Value',ax=ax3)
sns.distplot(Amar,hist=False,color='b',label='Predicted Value',ax=aa)
ax3.set_xlabel('Price')
ax3.set_ylabel('Proportion of cars')
ax3.set_title('Actual value vs Expected value')
plt.show()
