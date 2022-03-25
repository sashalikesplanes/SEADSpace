import numpy as np


R_mars = 3389.5e3
#R_mars = 6371e3  # m #radius of earth
G = 6.673e-11
M_mars = 6.39e23  # kg
#M_mars = 5.972e24 #mass of earth


def get_orbit_times(altitude):#ALTITUDE of orbit IN METERS
    R_orbit = R_mars +altitude
    V=np.sqrt((G*M_mars)/R_orbit)
    T=2*np.pi*R_orbit/V
    Theta = 2*np.arcsin(R_mars/R_orbit)#find angle of ecplise
    t_eclipse=(Theta/(2*np.pi))*T
    t_daylight=T-t_eclipse
    return t_daylight, t_eclipse#in seconds
