from star_sailor.simulator import propagate_mission, ode_fixed_orientation, Spacecraft
from star_sailor.vis import plot_trajectory_around_earth

from matplotlib import pyplot as plt
import matplotlib
import numpy as np

plt.style.use("dark_background")


def run_basic_mission():
    # Spacecraft in a 7000 km (SMA) circular orbit

    sc = Spacecraft(0.1, 10)

    t_span = (0, 30000)

    y0 = np.array([7000e3, 0, 0, 8e3])

    ode = ode_fixed_orientation(sc.area_over_mass, 0)

    # Propagate the spacecraft over the time span

    t, y = propagate_mission(ode, t_span, y0)

    # Plot the trajectory

    fig, ax = plt.subplots(figsize=(8, 8))

    plot_trajectory_around_earth(y, ax)

    ax.set_title("Trajectory")

    plt.show()
