import numpy as np

h = 800000  # height of orbit in m
R_mars = 3389.5e3  # m
R_orbit = R_mars+h
G = 6.673e-11
M_mars = 6.39e23  # kg

##FIND ORBITAL PERIOD FOR CIRCULAR ORBIT##
V=np.sqrt((G*M_mars)/R)
T = np.sqrt((4 * np.pi**2 * R_orbit**3)/(G*M_mars))


def get_orbit_times(altitude):

    t_daylight, t_eclipse = 0, 0
    return t_daylight, t_eclipse
