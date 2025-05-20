import cv2
import sys, os
import pyautogui
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from modules.detector import FaceLandmarkDetector
from modules.gaze_tracker import GazeTracker
from modules.wink_detector import WinkDetector
from modules.controller import CursorController  

def main():
    cap = cv2.VideoCapture(0)
    screen_width, screen_height = pyautogui.size()

    detector = FaceLandmarkDetector()
    gaze_tracker = GazeTracker()
    wink_detector = WinkDetector(blink_threshold=0.2, min_wink_duration=1.0)
    cursor_controller = CursorController(screen_width, screen_height)

    wink_display_time = 1.5  # seconds
    last_wink_time = 0
    last_wink_text = ''
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break

        frame_height, frame_width = frame.shape[:2]
        landmarks = detector.detect_landmarks(frame)

        if landmarks:
            # Gaze tracking
            gaze, left_iris, right_iris = gaze_tracker.estimate_gaze(landmarks, frame_width, frame_height)

            if gaze and left_iris and right_iris:
                iris_x_norm = (left_iris[0] + right_iris[0]) / 2 / frame_width
                iris_y_norm = (left_iris[1] + right_iris[1]) / 2 / frame_height
                cursor_controller.move_cursor_to_iris(iris_x_norm, iris_y_norm)

            # Wink click
            wink = wink_detector.detect_wink(landmarks, frame_width, frame_height)
            if wink:
                text = f"{wink.upper()} wink detected!"
                print(text)
                cursor_controller.click_if_wink(wink)
                last_wink_text = f'{wink.upper()} Wink Detected'
                last_wink_time = time.time()
            if time.time() - last_wink_time < wink_display_time:
               cv2.putText(frame, last_wink_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

        cv2.imshow("Eye Tracking Control", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
