import cv2

def resize_image(image, width=500):
    ratio = width / image.shape[1]
    dim = (width, int(image.shape[0] * ratio))
    return cv2.resize(image, dim)
