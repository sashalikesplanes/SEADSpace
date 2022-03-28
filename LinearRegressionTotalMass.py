import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#power-x  and mass-y

#reshape to column vector

def linregress():

    power_our_sat=1286
    mass=np.array([1030.5,725,1120,2180,1337.2,2454,4332])#launch mass
    power=np.array([980,750,460,2000,840,1200,2000]).reshape((-1,1))#power outputted by solar arrays

    model = LinearRegression().fit(power,mass)
    gradient=model.coef_
    intercept=model.intercept_

    x=np.linspace(400,2500,10000)
    y=gradient*x+intercept

    m_launch = gradient*power_our_sat+intercept
    plt.plot(x,y)
    plt.ylabel('Mass [kg]')
    plt.xlabel('Power [Watts]')
    plt.axvline(x=power_our_sat,color='r')
    plt.show()
    return m_launch

#using mass fraction from appendix A p.896 of SMEAD (remote sensing sats.)
m_launch=linregress()
print('m_launch:',m_launch)


#m_propellant=0.043*m_launch
m_dry_frac=0.418
m_dry=m_launch*m_dry_frac
#percentages of mass wrt to dry mass
payload_frac=0.346
structure_frac=0.189
thermal_frac=0.021
power_frac=0.243
TTC_frac=0.034
ADCS_frac=0.045
propulsion_frac=0.061



m_payload=payload_frac*m_dry 
m_structure=structure_frac*m_dry
m_thermal=thermal_frac*m_dry
m_power = power_frac*m_dry
m_TTC=TTC_frac*m_dry
m_ADCS=ADCS_frac*m_dry
m_prop=propulsion_frac*m_dry


print(m_dry, m_payload, m_structure, m_thermal,'m_power:', m_power, m_TTC, m_ADCS, m_prop)

