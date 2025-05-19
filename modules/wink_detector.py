import numpy as np

class WinkDetector:
    def __init__(self, threshold=4.0):
        self.threshold = threshold

    def eye_aspect_ratio(self, eye_landmarks, frame_width, frame_height):
        # Eye vertical distance
        y1 = int(eye_landmarks[1].y * frame_height)
        y2 = int(eye_landmarks[5].y * frame_height)
        vertical = abs(y2 - y1)

        # Eye horizontal distance
        x1 = int(eye_landmarks[0].x * frame_width)
        x2 = int(eye_landmarks[3].x * frame_width)
        horizontal = abs(x2 - x1)

        if horizontal == 0:
            return 0
        return vertical / horizontal

    def detect_wink(self, landmarks, frame_width, frame_height):
        LEFT_EYE = [33, 160, 158, 133, 153, 144]
        RIGHT_EYE = [362, 385, 387, 263, 373, 380]

        left_ear = self.eye_aspect_ratio([landmarks[i] for i in LEFT_EYE], frame_width, frame_height)
        right_ear = self.eye_aspect_ratio([landmarks[i] for i in RIGHT_EYE], frame_width, frame_height)

        if left_ear < 0.2 and right_ear >= 0.2:
            return "left"
        elif right_ear < 0.2 and left_ear >= 0.2:
            return "right"
        return None
