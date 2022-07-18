import os
import pandas as pd


def create_file_path_panda(parent_folders):
    paths = []
    for i in parent_folders:
        files = os.listdir(i)
        for j in files:
            path_to_current_file = i + "/" + j
            filename = j
            paths.append([path_to_current_file, filename])
    file_path_panda = pd.DataFrame(paths, columns=["path", "filename"])
    file_path_panda.to_csv("data_files/Mars Surface and Curiosity Image/all_images_file_paths.csv")
    return file_path_panda

