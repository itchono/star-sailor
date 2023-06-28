from dataclasses import dataclass


@dataclass
class Spacecraft:
    mass: float  # kg
    srp_area: float  # m^2

    @property
    def area_over_mass(self):
        return self.srp_area / self.mass
