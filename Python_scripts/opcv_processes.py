import cv2


# function takes a numpy array of image paths which are rgb images
# a save location for grayscale images and a save location for the
# lab images. Performs the conversion and then saves in those locations
def create_lab_files(image_paths, save_path_gray, save_path_colour):
    for i in image_paths:
        image_path = i[1]
        image_name = i[0]
        image = cv2.imread(image_path)
        lab_im = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
        (L, a, b) = cv2.split(lab_im)
        save_grey = save_path_gray + "/" + image_name
        cv2.imwrite(save_grey, L)
        save_colour = save_path_colour + "/" + image_name
        cv2.imwrite(save_colour, lab_im)
