import pandas as pd
import numpy as np
import os


def create_file_path_panda(parent_folders):
    image_paths = np.array([])
    for i in parent_folders:
        files = os.listdir(i)
        for j in files:
            path_to_current_file = i+j
            image_paths = np.append(image_paths, path_to_current_file)
    image_pandas = pd.DataFrame(image_paths)
    return image_pandas

