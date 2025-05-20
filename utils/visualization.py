import cv2
import numpy as np

# MediaPipe FaceMesh returns 468 facial landmarks
# Eye indices based on MediaPipe FaceMesh (approximate)
LEFT_EYE = [33, 133, 160, 159, 158, 157, 173, 153, 154, 155]
RIGHT_EYE = [362, 263, 387, 386, 385, 384, 398, 382, 381, 380]

def draw_landmarks(frame, landmarks, frame_width, frame_height):
    for idx, landmark in enumerate(landmarks):
        x, y = int(landmark.x * frame_width), int(landmark.y * frame_height) # Normalization
        cv2.circle(frame, (x, y), 1, (0, 255, 0), -1) #  small green dot at each landmark location

def draw_eye_boxes(frame, landmarks, frame_width, frame_height):
    for eye_indices in [LEFT_EYE, RIGHT_EYE]:
        points = []
        for idx in eye_indices:
            x = int(landmarks[idx].x * frame_width)
            y = int(landmarks[idx].y * frame_height)
            points.append((x, y))
        if len(points) >= 3:  # convexHull needs at least 3 points
            points_array = np.array(points, dtype=np.int32)
            hull = cv2.convexHull(points_array) # Computes the convex hull (smallest polygon that encloses all points)
            cv2.polylines(frame, [hull], isClosed=True, color=(255, 0, 0), thickness=1)