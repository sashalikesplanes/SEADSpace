import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#power-x  and mass-y

#reshape to column vector

def linregress():

    power_our_sat=500
    mass=np.array([1030.5,725,1120,2180,1337.2,2454,4332])#launch mass
    power=np.array([656,750,460,2000,840,1200,2000]).reshape((-1,1))#power outputted by solar arrays

    model = LinearRegression().fit(power,mass)
    gradient=model.coef_
    intercept=model.intercept_

    x=np.linspace(400,2500,10000)
    y=gradient*x+intercept
    plt.plot(x,y)
    plt.axvline(x=power_our_sat,color='r')
    plt.show()

#using mass fraction from appendix A p.896 of SMEAD (remote sensing sats.)
m_launch=1000 #kg
m_propellant=0.043*m_launch
m_dry=0.957*m_launch

#percentages of mass wrt to dry mass
payload_frac=0.346
structure_frac=0.189
thermal_frac=0.021
power_frac=0.243
TTC_frac=0.034
ADCS_frac=0.045
propulsion_frac=0.061

