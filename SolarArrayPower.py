import numpy as np

solar_param_dict = {
    "array_power": {
        # [W] power required by spacecraft in nominal
        "power_required_daylight": 800,
        # [W] power required by spacecraft in eclipse
        "power_required_eclipse": 400,
        "path_efficiency_daylight": 0.8,  # [-] total path efficiency daylight
        # [-] total path efficiency eclipse (includes through battery)
        "path_efficiency_eclipse": 0.6,
    },
    "lifetime_degradation": {
        "lifetime": 5,  # [years] total life time of mission
        # [-] efficiency lost per year of operation
        "degradation_per_year": 0.05,
    },
    "power_per_area_EOL": {
        "angle_of_incidence": 5,  # [deg] worst case angle of incidence
        # [-] fraction of solar incidence captured by array, varies per type
        "power_conversion_efficiency": 0.148,
        # [W/m^2] solar incidence radiation at location
        "solar_radiation_per_area": 1000,
        # [-] factor to account for the inherent degradation of solar panel
        "inherent_degradation": 0.9,
    }
}


def get_area_solar(params):
    t_daylight, t_eclipse = get_orbit_times(orbit_altitude)
    params["t_daylight"] = t_daylight
    params['t_eclipse'] = t_eclipse
    power_solar = get_array_power(**params["array_power"])
    lifetime_degradation = get_lifetime_degradation(
        **params["lifetime_degradation"])
    power_per_area_EOL = get_power_per_area_EOL(
        lifetime_degradation=lifetime_degradation, **params["power_per_area_EOL"])
    return power_solar / power_per_area_EOL


def get_array_power(power_required_daylight, power_required_eclipse, t_eclipse, t_daylight, path_efficiency_daylight, path_efficiency_eclipse):
    """
    Computes the power that must be generated by solar cells based on:
    power_daylight - power to be delivered to spacecraft during nominal conditions
    power_eclipse - power to be delivered to spacecraft during eclipse conditions
    t_daylight - time the spacecraft is in nominal conditions
    t_eclipse - time the spacecraft is in eclipse condition
    path_efficiency_daylight - from array to space craft in nominal conditions
    path_efficiency_eclipse - from array to space craft (through batter!) in eclipse condition
    """

    return (((power_required_daylight * t_daylight) / path_efficiency_daylight)
            + (power_required_eclipse * t_eclipse) / path_efficiency_eclipse) / t_daylight


def get_lifetime_degradation(lifetime, degradation_per_year):
    # Computes total life time degradation factor
    # Lifetime in years
    return (1 - degradation_per_year) ** lifetime


def get_power_per_area_EOL(angle_of_incidence, solar_radiation_per_area, power_conversion_efficiency, inherent_degradation, lifetime_degradation):
    # Compute power per square meter at eng of life
    # angle_of_incidece of solar radiation in degrees!
    # inherent_degradation factor
    # lifetime_degradation factor
    # power_per_area nominal
    power_per_area_0 = solar_radiation_per_area * power_conversion_efficiency
    power_per_area_BOL = power_per_area_0 * inherent_degradation * \
        np.cos(angle_of_incidence / 180 * np.pi)
    return power_per_area_BOL * lifetime_degradation


if __name__ == "__main__":
    print(get_area_solar(solar_param_dict))
