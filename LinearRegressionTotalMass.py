import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#power-x  and mass-y

m=np.array([1030.5,725,1120,2180,1337.2,2454,4332])
power=np.array([656,750,460,2000,840,1200,2000]).reshape((-1,1))#reshape to column vector
model = LinearRegression().fit(power,m)

gradient=model.coef_
intercept=model.intercept_

x=np.linspace(400,2500,10000)
y=gradient*x+intercept
plt.plot(x,y)
plt.show()