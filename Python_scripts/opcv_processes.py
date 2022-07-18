import cv2


def create_Lab_files(image_paths, save_path_grey, save_path_colour):
    for i in image_paths:
        image_path = i[1]
        image_name = i[0]
        image = cv2.imread(image_path)
        lab_im = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
        (L, a, b) = cv2.split(lab_im)
        save_grey = save_path_grey + "/" + image_name
        cv2.imwrite(save_grey, L)
        save_colour = save_path_colour + "/" + image_name
        cv2.imwrite(save_colour, lab_im)
