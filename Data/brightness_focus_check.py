# import cv2
# import numpy as np

# def check_brightness_and_focus(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     brightness = np.mean(gray)
#     focus_measure = cv2.Laplacian(gray, cv2.CV_64F).var()
    
#     brightness_ok = 100 < brightness < 200
#     focus_ok = focus_measure > 100

#     return brightness_ok, focus_ok

import cv2
import numpy as np

def check_brightness_and_focus(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    focus_measure = cv2.Laplacian(gray, cv2.CV_64F).var()
    
    brightness_ok = 100 < brightness < 200
    focus_ok = focus_measure > 100

    return brightness_ok, focus_ok