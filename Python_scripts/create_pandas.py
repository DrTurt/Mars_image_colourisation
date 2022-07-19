import os
import pandas as pd


# Function takes a list of file paths to parent folders
# then regardless of the type of file, creates a pandas
# table containing all of those file paths and file names.
def create_file_path_panda(parent_folders):
    paths = []
    for i in parent_folders:
        files = os.listdir(i)
        for j in files:
            path_to_current_file = i + "/" + j
            filename = j
            paths.append([path_to_current_file, filename])
    file_path_panda = pd.DataFrame(paths, columns=["path", "filename"])
    return file_path_panda
