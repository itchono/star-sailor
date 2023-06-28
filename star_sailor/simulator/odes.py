from typing import Callable

import numpy as np

from star_sailor.dyn_2d import gravity
from star_sailor.dyn_2d import srp

ODEType = Callable[[float, np.ndarray], np.ndarray]


def ode_fixed_orientation(area_over_mass: float, orientation: float) -> ODEType:
    """
    Returns the ODE for the solar sail spacecraft with a fixed orientation.
    """

    def ode(t: float, y: np.ndarray):
        """
        Returns the derivative of the state vector y at time t.

        Parameters
        ----------
        t : float
            The time
        y : np.ndarray
            The state vector [x y vx vy]

        Returns
        -------
        np.ndarray
            The derivative of the state vector [vx vy ax ay]
        """
        state = y[:4]

        accel_gravity = gravity.earth_gravity(state)
        accel_srp = srp.solar_radiation_pressure(state, orientation, area_over_mass)

        return np.concatenate([state[2:], accel_gravity + accel_srp])

    return ode
