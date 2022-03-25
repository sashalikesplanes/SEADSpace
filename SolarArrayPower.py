import numpy as np


def get_array_power(power_daylight, power_eclipse, t_daylight, t_eclipse, path_efficiency_daylight, path_efficiency_eclipse):
    """
    Computes the power that must be generated by solar cells based on:
    power_daylight - power to be delivered to spacecraft during nominal conditions
    power_eclipse - power to be delivered to spacecraft during eclipse conditions
    t_daylight - time the spacecraft is in nominal conditions
    t_eclipse - time the spacecraft is in eclipse condition
    path_efficiency_daylight - from array to space craft in nominal conditions
    path_efficiency_eclipse - from array to space craft (through batter!) in eclipse condition
    """

    return (((power_daylight * t_daylight) / path_efficiency_daylight)
            + (power_eclipse * t_eclipse) / path_efficiency_eclipse) / t_daylight


def get_lifetime_degradation(lifetime, degradation_per_year):
    # Computes total life time degradation factor
    # Lifetime in years
    return (1 - degradation_per_year) ** lifetime


def get_power_per_area_EOL(angle_of_incidence, power_per_area_0, inherent_degradation, lifetime_degradation):
    # Compute power per square meter at eng of life
    # angle_of_incidece of solar radiation in degrees!
    # inherent_degradation factor
    # lifetime_degradation factor
    # power_per_area nominal
    power_per_area_BOL = power_per_area_0 * inherent_degradation * \
        np.cos(angle_of_incidence / 180 * np.pi)
    return power_per_area_BOL * lifetime_degradation
