import numpy as np

h=800000 #height of orbit in m
R_mars=3389.5*10**3 #m
R_orbit=R_mars+(h)/2
G=6.673*10**(-11)
M_mars=6.39*10**23 #kg

##FIND ORBITAL PERIOD FOR CIRCULAR ORBIT##
T=np.sqrt((4 * np.pi**2 * R_orbit**3)/(G*M_mars))