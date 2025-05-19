import cv2, sys, os
import pyautogui
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.detector import FaceLandmarkDetector
from modules.gaze_tracker import GazeTracker
from modules.controller import CursorController

def run_test():
    cap = cv2.VideoCapture(0)
    detector = FaceLandmarkDetector()
    gaze_tracker = GazeTracker()
    screen_width, screen_height = pyautogui.size()
    controller = CursorController(screen_width, screen_height)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break

        frame_height, frame_width = frame.shape[:2]
        landmarks = detector.detect_landmarks(frame)

        if landmarks:
            _, left_iris, _ = gaze_tracker.estimate_gaze(landmarks, frame_width, frame_height)
            if left_iris:
                iris_x_norm = left_iris[0] / frame_width
                iris_y_norm = left_iris[1] / frame_height
                controller.move_cursor_to_iris(iris_x_norm, iris_y_norm)

        cv2.imshow("Cursor Control Only", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_test()
