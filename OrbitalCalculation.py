import numpy as np

R_mars = 3389.5e3
G = 6.673e-11
M_mars = 6.39e23  # kg

mu_mars=G*M_mars
J2=1960.45e-6
rho=(2*np.pi)/(31536000*1.88) #mean motion of mars around sun


def get_orbit_times(altitude):#ALTITUDE of orbit IN METERS
    R_orbit = R_mars +altitude

    i=np.arccos((-2*rho*R_orbit**(7/2))/(3*J2*R_mars**2 * np.sqrt(mu_mars)))#inclination angle for sun synchronous orbit at altitude of 800km
    
    V=np.sqrt((G*M_mars)/R_orbit)
    print(V)
    T=2*np.pi*R_orbit/V
    
    Theta = 2*np.arcsin(R_mars/R_orbit)#find angle of ecplise
    t_eclipse=(Theta/(2*np.pi))*T
    t_daylight=T-t_eclipse

    print(T)
    print(t_eclipse)
    print(i*180/np.pi)
    
    return t_daylight, t_eclipse, i*180/np.pi

get_orbit_times(800000)

