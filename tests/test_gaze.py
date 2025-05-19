import cv2, os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.detector import FaceLandmarkDetector
from modules.gaze_tracker import GazeTracker

def run_test():
    cap = cv2.VideoCapture(0)
    detector = FaceLandmarkDetector()
    gaze_tracker = GazeTracker()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_height, frame_width = frame.shape[:2]
        landmarks = detector.detect_landmarks(frame)

        if landmarks:
            gaze, left_iris, right_iris = gaze_tracker.estimate_gaze(landmarks, frame_width, frame_height)
            if left_iris:
                cv2.circle(frame, left_iris, 3, (0, 255, 255), -1)
            if right_iris:
                cv2.circle(frame, right_iris, 3, (0, 255, 255), -1)

            text = f"Left Eye: {gaze['left']} | Right Eye: {gaze['right']}"
            cv2.putText(frame, text, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Gaze Tracker Test", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_test()