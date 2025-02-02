# import cv2

# def capture_image():
#     cap = cv2.VideoCapture(0)
#     while True:
#         ret, frame = cap.read()
#         if ret:
#             cv2.imshow('Camera Feed', frame)
#         if cv2.waitKey(1) & 0xFF == ord('c'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#     return frame

# import cv2
# from Data.brightness_focus_check import check_brightness_and_focus
# from Data.face_detection import detect_face

# def capture_image():
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         raise IOError("Cannot open webcam")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             raise IOError("Failed to capture image")

#         # Real-time checks
#         brightness_ok, focus_ok = check_brightness_and_focus(frame)
#         faces = detect_face(frame)

#         # Display checkboxes
#         status_color = (0, 255, 0) if brightness_ok else (0, 0, 255)
#         cv2.putText(frame, f"Lighting: {'OK' if brightness_ok else 'Unknown'}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)

#         status_color = (0, 255, 0) if len(faces) > 0 else (0, 0, 255)
#         cv2.putText(frame, f"Area: {'OK' if len(faces) > 0 else 'Unknown'}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)

#         frontal_ok = len(faces) > 0  # Simplified frontal face detection assumption
#         status_color = (0, 255, 0) if frontal_ok else (0, 0, 255)
#         cv2.putText(frame, f"Frontal: {'OK' if frontal_ok else 'Unknown'}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)

#         cv2.imshow('Camera Feed', frame)
#         if cv2.waitKey(1) & 0xFF == ord('c'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     return frame

import cv2
from Data.brightness_focus_check import check_brightness_and_focus
from Data.face_detection import detect_face

def capture_image():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            brightness_ok, focus_ok = check_brightness_and_focus(frame)
            faces = detect_face(frame)

            lighting_status = "OK" if brightness_ok else "Unknown"
            area_status = "OK" if len(faces) > 0 else "Unknown"
            frontal_status = "OK" if len(faces) > 0 else "Unknown"

            cv2.putText(frame, f'Lighting: {lighting_status}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0) if brightness_ok else (0, 0, 255), 2)
            cv2.putText(frame, f'Area: {area_status}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0) if area_status == "OK" else (0, 0, 255), 2)
            cv2.putText(frame, f'Frontal: {frontal_status}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0) if frontal_status == "OK" else (0, 0, 255), 2)

            cv2.imshow('Camera Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return frame