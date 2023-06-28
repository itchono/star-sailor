from __future__ import annotations

from star_sailor.simulator.odes import ODEType
from scipy.integrate import solve_ivp

import numpy as np


def propagate_mission(
    ode: ODEType,
    t_span: np.ndarray,
    y0: np.ndarray,
    solver: str = "DOP853",
) -> tuple[np.ndarray, np.ndarray]:
    """
    Propagates the spacecraft state vector over the given time span.

    Parameters
    ----------
    spacecraft : Spacecraft
        The spacecraft
    ode : ODEType
        The ODE governing the spacecraft dynamics

    t_span : np.ndarray
        The time span to propagate over, in seconds

    y0 : np.ndarray
        The initial state vector [x y vx vy] (inertial)

    solver : str
        The solver to use, default is "DOP853"

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        The time and state vectors
        time array of shape (n,)
        state array of shape (n, 4)
    """
    sol = solve_ivp(ode, t_span, y0, method=solver, rtol=1e-12, atol=1e-12)

    return sol.t, sol.y.T
