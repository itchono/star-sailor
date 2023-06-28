import numpy as np

from star_sailor.constants import R_EARTH, SUN_POSITION


def r_sun_rel_spacecraft(state: np.ndarray) -> np.ndarray:
    """
    Returns the position of the sun relative to the spacecraft.

    Parameters
    ----------
    state : np.ndarray
        The state vector of the spacecraft [x y vx vy]

    Returns
    -------
    np.ndarray
        The position of the sun relative to the spacecraft [x y]
    """
    return SUN_POSITION - state[:2]


def is_occluded_by_earth(state: np.ndarray) -> bool:
    """
    Returns true if the spacecraft is shadowed from the Sun by the Earth.

    Parameters
    ----------
    state : np.ndarray
        The state vector of the spacecraft [x y vx vy]

    Returns
    -------
    bool
        True if the spacecraft is shadowed from the Sun by the Earth.
    """
    r_sun_rel_eci = SUN_POSITION
    r_spacecraft = state[:2]

    # Curtis, algorithm 12.3
    r = np.linalg.norm(r_spacecraft)
    r_s = np.linalg.norm(r_sun_rel_eci)
    theta = np.arccos(r_spacecraft @ r_sun_rel_eci / (r * r_s))
    theta_1 = np.arccos(R_EARTH / r)
    theta_2 = np.arccos(R_EARTH / r_s)

    return theta < theta_1 + theta_2
