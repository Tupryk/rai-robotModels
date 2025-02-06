import rowan
import numpy as np
import robotic as ry
from load_random_plys import load_single_from_type


if __name__ == "__main__":

    C = ry.Config()

    C = load_single_from_type(C, pos=[.0, .0, .5], rot=rowan.from_euler(np.pi, 0, 0), root_path="rai_jointed/fixtures/stoves/coil_burners_induc")

    C.view(True)
    C.animate()
    C.view(True)
    