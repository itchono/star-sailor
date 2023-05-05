import numpy as np

from star_sailor.constants import GM_EARTH


def earth_gravity(state: np.ndarray) -> np.ndarray:
    """
    Returns the acceleration due to gravity at the given state.

    Parameters
    ----------
    state : np.ndarray
        The state vector of the spacecraft [x y vx vy]

    Returns
    -------
    np.ndarray
        The acceleration due to gravity at the given state. [ax ay]
    """
    position = state[:2]
    radius = np.linalg.norm(position)

    return -GM_EARTH * position / radius**3
