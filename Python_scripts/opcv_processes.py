import cv2


def create_greyscales(image_paths, save_path):
    for i in image_paths:
        image_path = i[0]
        image_name = i[1]
        image = cv2.imread(image_path)
        lab_im = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
        gray_im = lab_im
        save_file = save_path + "/" + image_name
        cv2.imwrite(save_file, grey_im)
