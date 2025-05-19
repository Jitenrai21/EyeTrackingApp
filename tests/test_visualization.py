import cv2, os, sys
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.detector import FaceLandmarkDetector
from utils.visualization import draw_landmarks, draw_eye_boxes

def run_test():
    detector = FaceLandmarkDetector()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_height, frame_width = frame.shape[:2]
        landmarks = detector.detect_landmarks(frame)

        if landmarks:
            draw_landmarks(frame, landmarks, frame_width, frame_height)
            draw_eye_boxes(frame, landmarks, frame_width, frame_height)

        cv2.imshow("Test - Visualization", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_test()
