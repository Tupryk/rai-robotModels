import os
import numpy as np
import robotic as ry


if __name__ == "__main__":

    root_path = "rai_jointed"

    g_files = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith('.g'):
                g_path = os.path.join(root, file)
                with open(g_path, "r") as file:
                    lines = file.read()
                    if "joint" in  lines:
                        g_files.append(g_path)

    print(len(g_files))

    # selected_file = np.random.choice(g_files, 1, replace=False)[0]

    # print(selected_file)

    # C = ry.Config()
    # C.addFile(selected_file)
    # C.view(True)
    # C.animate()

    for g in g_files:
        C = ry.Config()
        C.addFile(g)
        C.view(True)
        C.animate()
