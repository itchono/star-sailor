from star_sailor.constants import SOLAR_PHOTON_PRESSURE
from star_sailor.ephemeris_2d.solar import r_sun_rel_spacecraft, is_occluded_by_earth
import numpy as np


def solar_radiation_pressure(
    state: np.ndarray, orientation_angle: float, area_over_mass: float
) -> np.ndarray:
    """
    Returns the acceleration due to solar radiation pressure at the given state,
    and given a control input of the orientation angle of the spacecraft.

    Parameters
    ----------
    state : np.ndarray
        The state vector of the spacecraft [x y vx vy]
    orientation_angle : float
        The orientation angle of the spacecraft in radians

    Returns
    -------
    np.ndarray
        The acceleration due to solar radiation pressure at the given state. [ax ay]
    """
    # Check if the spacecraft is occluded by the Earth
    if is_occluded_by_earth(state):
        return np.zeros(2)

    solar_sail_normal = np.array([np.cos(orientation_angle), np.sin(orientation_angle)])

    rsrs = r_sun_rel_spacecraft(state)

    if rsrs @ solar_sail_normal < 0:
        # The solar sail is not facing the sun
        solar_sail_normal = -solar_sail_normal

    alpha = np.arccos(rsrs @ solar_sail_normal / np.linalg.norm(rsrs))

    magnitude = SOLAR_PHOTON_PRESSURE * area_over_mass * np.cos(alpha) ** 2

    return magnitude * solar_sail_normal
