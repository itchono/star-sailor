import numpy as np

# Gravitational constant of Earth
GM_EARTH = 3.986004418e14  # m^3/s^2
R_EARTH = 6371000.0  # m

# Fixed sun location wrt Earth
# 1 AU from Earth, in the direction of the vernal equinox
SUN_POSITION = np.array([-1.471009e11, 0.0])  # m
SOLAR_PHOTON_PRESSURE = 4.56e-6  # N/m^2
