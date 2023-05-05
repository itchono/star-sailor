# Star Sailor - Solar Sail Dynamics Simulator

This is a project to kick off my 4th year undergraduate thesis. The goal of this simulator is for me to develop an intuition for working with solar sails and to develop a tool that can be used to simulate the dynamics of a solar sail in a variety of scenarios. The code in here will be used later one to help me develop a steering law for trajectory optimization.

## Getting Started

Star Sailor runs on [PyPy](https://pypy.org/), which speeds up regular Python code. I am using this to compare against my previous projects built on regular Python, ctypes, and cffi. However, the code should be drop-in compatible with regular Python 3.8+.

To install, simply run `pip install git+https://github.com/itchono/star-sailor`. This will install the package and all of its dependencies. To run the simulator, simply run `python -m star-sailor`.

If installing on PyPy, use PyPy 3.8, and add the flag `--extra-index-url https://antocuni.github.io/pypy-wheels/manylinux2010/` to the `pip install` command.

## Dynamics
Star sailor is a 2D simulator using Cowell's method of propagation with the following accelerations:

### Solar Radiation Pressure
$$a_{\text{SRP}} = \left[2 P_{\text{Sun}} \cdot \frac{A}{m} \cdot \cos^2 \alpha \right] \hat{n}$$
where $P_{\text{Sun}}$ is the solar irradiance at 1 AU, $A$ is the area of the sail, $m$ is the mass of the sail, and $\alpha$ is the angle between the sail normal ($\hat{n}$) and the sun vector.

This is for an ideal sail, which is perfectly reflective.

### Gravity
$$a_{\text{grav}} = -\frac{\mu}{r^3} \boldsymbol{r}$$
where $\mu$ is the gravitational parameter of the central body, and $\vec{r}$ is the position vector of the spacecraft relative to the central body.

This is for a spherical central body (i.e. without J2 effects).

## Integration
Time integration is done using the [Dormand-Prince 8(7) method](https://en.wikipedia.org/wiki/Dormand%E2%80%93Prince_method) with a variable step size. The error tolerance is set to $10^{-12}$. The integration is done using the [SciPy](https://www.scipy.org/) library. However, I am also looking at making my own integrator using extrapolation methods.

