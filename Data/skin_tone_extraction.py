# import cv2

# def detect_face(image):
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#     return faces

# # skin_tone_extraction.py

# import numpy as np

# def extract_skin_tone(image):
#     hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     mean_hue = np.mean(hsv_image[:, :, 0])

#     if mean_hue < 15:
#         return 'Type I'
#     elif mean_hue < 30:
#         return 'Type II'
#     elif mean_hue < 45:
#         return 'Type III'
#     elif mean_hue < 60:
#         return 'Type IV'
#     elif mean_hue < 75:
#         return 'Type V'
#     else:
#         return 'Type VI'

import cv2
import numpy as np

def extract_skin_tone(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mean_hue = np.mean(hsv_image[:, :, 0])

    if mean_hue < 15:
        return "Type 1 - Very fair (Pale)"
    elif mean_hue < 30:
        return "Type 2 - Fair"
    elif mean_hue < 45:
        return "Type 3 - Light to medium"
    elif mean_hue < 60:
        return "Type 4 - Medium brown"
    elif mean_hue < 75:
        return "Type 5 - Dark brown"
    else:
        return "Type 6 - Deeply pigmented (Darkest)"