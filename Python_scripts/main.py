from create_pandas import *
from opcv_processes import *
import os
import pandas as pd

if __name__ == '__main__':

    print("This code will be for Mars image processing and colourisation.")

    all_images_path = "data_files/Mars Surface and Curiosity Image/all_images_file_paths.csv"
    if os.path.exists(all_images_path):
        image_paths = pd.read_csv(all_images_path, index_col=0)
    else:
        image_paths = create_file_path_panda(["data_files/Mars Surface and Curiosity Image/additional_images",
                                              "data_files/Mars Surface and Curiosity Image/images"])

    if len(os.listdir("data_files/Mars Surface and Curiosity Image/greyscales")) == 0:
        create_greyscales(image_paths.to_numpy(), "data_files/Mars Surface and Curiosity Image/greyscales")

    #print(len(image_paths.columns))
    if len(image_paths.columns) < 3:
        grey_paths = create_file_path_panda(["data_files/Mars Surface and Curiosity Image/greyscales"])
        image_paths['grayscale_path'] = grey_paths["path"]
        cols = ["filename", "path", "grayscale_path"]
        image_paths = image_paths[cols]
        image_paths.to_csv(all_images_path)

    print("DEBUG")
