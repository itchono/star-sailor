from matplotlib.patches import Circle
from matplotlib.axes import Axes
import numpy as np

from star_sailor.constants import R_EARTH


def make_axis_suitable(ax: Axes) -> None:
    """
    Makes an axis suitable for plotting a spacecraft trajectory around the Earth
    - Equal aspect ratio
    """
    ax.set_aspect("equal")


def plot_earth_on_axes(ax: Axes) -> None:
    """
    Plots the Earth on the given axes
    """
    patch = Circle((0, 0), R_EARTH, color="C0")
    ax.add_patch(patch)


def add_start_and_end_markers(y: np.ndarray, ax: Axes) -> None:
    """
    Adds start and end markers to the given axes
    """
    ax.scatter(y[0, 0], y[0, 1], color="green", marker="x", label="Start")
    ax.scatter(y[-1, 0], y[-1, 1], color="red", marker="x", label="End")


def plot_trajectory_around_earth(y: np.ndarray, ax: Axes) -> None:
    """
    Plots a spacecraft trajectory around the Earth
    """
    make_axis_suitable(ax)
    plot_earth_on_axes(ax)

    ax.plot(y[:, 0], y[:, 1], color="white")
    add_start_and_end_markers(y, ax)

    ax.legend()
