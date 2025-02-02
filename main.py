# from Data.brightness_focus_check import check_brightness_and_focus
# from Data.color_suggestion import suggest_color
# from Data.face_detection import detect_face
# from Data.skin_tone_extraction import extract_skin_tone
# from UI.camera_feed import capture_image
# from UI.display import display_message
# from Utils.helper import resize_image

# def main():
#     image = capture_image()
#     image = resize_image(image)
    
#     brightness_ok, focus_ok = check_brightness_and_focus(image)
#     if not (brightness_ok and focus_ok):
#         display_message("Image does not meet brightness or focus requirements.")
#         return

#     faces = detect_face(image)
#     if len(faces) == 0:
#         display_message("No face detected.")
#         return

#     skin_tone = extract_skin_tone(image)
#     color_suggestion = suggest_color(skin_tone)

#     display_message(f"Detected skin tone: {skin_tone}")
#     display_message(f"Suggested colors: {color_suggestion}")

# if __name__ == "__main__":
#     main()


# from Data.brightness_focus_check import check_brightness_and_focus
# from Data.color_suggestion import suggest_color
# from Data.face_detection import detect_face
# from Data.skin_tone_extraction import extract_skin_tone
# from UI.camera_feed import capture_image
# from UI.display import display_message
# from Utils.helper import resize_image

# def main():
#     try:
#         image = capture_image()
#         image = resize_image(image)

#         brightness_ok, focus_ok = check_brightness_and_focus(image)
#         if not (brightness_ok and focus_ok):
#             display_message("Image does not meet brightness or focus requirements.")
#             return

#         faces = detect_face(image)
#         if len(faces) == 0:
#             display_message("No face detected.")
#             return

#         skin_tone = extract_skin_tone(image)
#         color_suggestion = suggest_color(skin_tone)

#         display_message(f"Detected skin tone: {skin_tone}")
#         display_message(f"Suggested colors: {color_suggestion}")

#     except Exception as e:
#         display_message(f"An error occurred: {str(e)}")

# if __name__ == "__main__":
#     main()


# from Data.brightness_focus_check import check_brightness_and_focus
# from Data.color_suggestion import suggest_color
# from Data.face_detection import detect_face
# from Data.skin_tone_extraction import extract_skin_tone
# from UI.camera_feed import capture_image
# from UI.display import display_message
# from Utils.helper import resize_image

# def main():
#     image = capture_image()
#     image = resize_image(image)
    
#     brightness_ok, focus_ok = check_brightness_and_focus(image)
#     if not (brightness_ok and focus_ok):
#         display_message("Image does not meet brightness or focus requirements.")
#         return

#     faces = detect_face(image)
#     if len(faces) == 0:
#         display_message("No face detected.")
#         return

#     skin_tone = extract_skin_tone(image)
#     color_suggestion = suggest_color(skin_tone)

#     display_message(f"Detected skin tone: {skin_tone}")
#     display_message(f"Suggested colors: {color_suggestion}")

# if __name__ == "__main__":
#     main()

# from Data.brightness_focus_check import check_brightness_and_focus
# from Data.color_suggestion import suggest_color
# from Data.face_detection import detect_face
# from Data.skin_tone_extraction import extract_skin_tone
# from Data.body_type_analysis import determine_body_type
# from UI.camera_feed import capture_image
# from UI.display import display_message
# from Utils.helper import resize_image

# def main():
#     image = capture_image()
#     image = resize_image(image)

#     brightness_ok, focus_ok = check_brightness_and_focus(image)
#     if not (brightness_ok and focus_ok):
#         display_message("Image does not meet brightness or focus requirements.")
#         return

#     faces = detect_face(image)
#     if len(faces) == 0:
#         display_message("No face detected.")
#         return

#     skin_tone = extract_skin_tone(image)
#     color_suggestion = suggest_color(skin_tone)

#     display_message(f"Detected skin tone: {skin_tone}")
#     display_message(f"Suggested colors: {color_suggestion}")

#     # Body Dimensions Upload
#     dimensions = {
#         'bust': float(input("Enter bust measurement (in cm): ")),
#         'waist': float(input("Enter waist measurement (in cm): ")),
#         'hips': float(input("Enter hips measurement (in cm): "))
#     }

#     body_type = determine_body_type(dimensions)
#     display_message(f"Determined body type: {body_type}")

# if __name__ == "__main__":
#     main()

from Data.brightness_focus_check import check_brightness_and_focus
from Data.color_suggestion import suggest_color
from Data.face_detection import detect_face
from Data.skin_tone_extraction import extract_skin_tone
from Data.body_type_analysis import determine_body_type, suggest_outfits
from UI.camera_feed import capture_image
from UI.display import display_message
from Utils.helper import resize_image

def main():
    image = capture_image()
    image = resize_image(image)

    brightness_ok, focus_ok = check_brightness_and_focus(image)
    if not (brightness_ok and focus_ok):
        display_message("Image does not meet brightness or focus requirements.")
        return

    faces = detect_face(image)
    if len(faces) == 0:
        display_message("No face detected.")
        return

    skin_tone = extract_skin_tone(image)
    color_suggestion = suggest_color(skin_tone)

    display_message(f"Detected skin tone: {skin_tone}")
    display_message(f"Suggested colors: {color_suggestion}")

    # Body Dimensions Upload
    dimensions = {
        'bust': float(input("Enter bust measurement (in cm): ")),
        'waist': float(input("Enter waist measurement (in cm): ")),
        'hips': float(input("Enter hips measurement (in cm): "))
    }

    body_type = determine_body_type(dimensions)
    display_message(f"Determined body type: {body_type}")

    outfit_suggestions = suggest_outfits(body_type)
    for category, suggestion in outfit_suggestions.items():
        display_message(f"{category} suggestions: {suggestion}")

if __name__ == "__main__":
    main()
