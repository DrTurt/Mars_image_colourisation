from create_pandas import *
from opcv_processes import *


def lab_file_creation():
    # pull the files from curiosity images from the images and additional_images
    # folders, and create a pandas table containing all of the file names and
    # file paths to the images.
    all_images_path = "data_files/curiosity_images/all_images_file_paths.csv"
    if os.path.exists(all_images_path):
        image_paths = pd.read_csv(all_images_path, index_col=0)
    else:
        # function from create_pandas.py used to make the table.
        image_paths = create_file_path_panda(["data_files/curiosity_images/additional_images",
                                              "data_files/curiosity_images/images"])
        image_paths.to_csv(all_images_path)

    # first check if directories exist to store grayscale and lab images
    # if they exist, then the files have most likely already been created
    # then create the images and save them if necessary.
    grays_path = "data_files/curiosity_images/grayscale_images"
    labs_path = "data_files/curiosity_images/full_lab_images"
    if not os.path.exists(grays_path):
        os.mkdir(grays_path)
    if not os.path.exists(labs_path):
        os.mkdir(labs_path)
    if len(os.listdir(grays_path)) == 0 or len(os.listdir(labs_path)) == 0:
        # function from opcv_processes.py used to convert rgb to lab and save the files.
        create_lab_files(image_paths.to_numpy(), grays_path, labs_path)

    # edit the original pandas table to contain the file paths for the
    # grayscale and lab images too.
    # print(len(image_paths.columns))
    if len(image_paths.columns) < 4:
        gray_paths = create_file_path_panda([grays_path])
        lab_paths = create_file_path_panda([labs_path])
        image_paths['grayscale_path'] = gray_paths["path"]
        image_paths['Lab_path'] = lab_paths["path"]
        cols = ["filename", "path", "Lab_path", "grayscale_path"]
        image_paths = image_paths[cols]
        image_paths.to_csv(all_images_path)

    return image_paths


if __name__ == '__main__':
    # print a short message saying what the code should do, and to verify
    # that the main function is what is running.
    print("This code performs Mars image processing and colourisation using openCV and a convolutional neural network.")

    # initially the current working directory is "python_scripts" but it
    # needs to be changed to the parent folder for more sensible local
    # file paths
    os.chdir("C:/Users/lul12/uni/PhD/Mars_image_colourisation/Mars_image_colourisation")
    print("Current working directory:", os.getcwd())

    # run the creation of lab files and the pandas dataframe, which is then
    # returned as part of this function.
    image_path_pandas = lab_file_creation()

    print("DEBUG")
