import cv2, sys, os, pyautogui
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.detector import FaceLandmarkDetector
from modules.wink_detector import WinkDetector

def run_test():
    cap = cv2.VideoCapture(0)
    detector = FaceLandmarkDetector()
    wink_detector = WinkDetector(blink_threshold=0.2, min_wink_duration=1.0)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break

        frame_height, frame_width = frame.shape[:2]
        landmarks = detector.detect_landmarks(frame)

        if landmarks:
            wink = wink_detector.detect_wink(landmarks, frame_width, frame_height)
            if wink:
                print(f"Wink Detected: {wink.upper()}")

                if wink == 'left':
                    pyautogui.click(button='left')
                    time.sleep(1)  # Short delay to prevent rapid repeat

                elif wink == 'right':
                    pyautogui.click(button='right')
                    time.sleep(1)

        cv2.imshow("Wink Detection with Click", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_test()
