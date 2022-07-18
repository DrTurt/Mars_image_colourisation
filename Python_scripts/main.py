from create_pandas import *
from opcv_processes import *
import os
import pandas as pd

def Lab_file_creation():
    all_images_path = "data_files/curiosity_images/all_images_file_paths.csv"
    if os.path.exists(all_images_path):
        image_paths = pd.read_csv(all_images_path, index_col=0)
    else:
        image_paths = create_file_path_panda(["data_files/curiosity_images/additional_images",
                                              "data_files/curiosity_images/images"])
        image_paths.to_csv("data_files/curiosity_images/all_images_file_paths.csv")

    if len(os.listdir("data_files/curiosity_images/greyscales")) == 0 \
    or len(os.listdir("data_files/curiosity_images/full_lab_images")) == 0:
        create_Lab_files(image_paths.to_numpy(), "data_files/curiosity_images/greyscales",
                                                 "data_files/curiosity_images/full_lab_images")

    # print(len(image_paths.columns))
    if len(image_paths.columns) < 4:
        grey_paths = create_file_path_panda(["data_files/curiosity_images/greyscales"])
        lab_paths = create_file_path_panda(["data_files/curiosity_images/full_lab_images"])
        image_paths['grayscale_path'] = grey_paths["path"]
        image_paths['Lab_path'] = lab_paths["path"]
        cols = ["filename", "path", "Lab_path", "grayscale_path"]
        image_paths = image_paths[cols]
        image_paths.to_csv(all_images_path)

if __name__ == '__main__':

    print("This code performs Mars image processing and colourisation using openCV and a convolutional neural network.")

    os.chdir("C:/Users/lul12/uni/PhD/Mars_image_colourisation/Mars_image_colourisation")
    print("Current working directory:", os.getcwd())

    Lab_file_creation()

    print("DEBUG")
