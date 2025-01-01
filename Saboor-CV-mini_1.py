import cv2
import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc
import numpy as np

# Initialize MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2
)
Draw = mp.solutions.drawing_utils

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Convert the frame to RGB as MediaPipe works with RGB images
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            Draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

            thumb_tip = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]

            # Get coordinates for thumb and index fingers
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)

            # Draw circles at thumb and index fingers
            cv2.circle(frame, (thumb_x, thumb_y), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED)

            # Draw a line between thumb and index finger
            cv2.line(frame, (thumb_x, thumb_y), (index_x, index_y), (0, 255, 255), 2)

            # Calculate the distance between thumb and index finger
            distance = hypot(index_x - thumb_x, index_y - thumb_y)

            # Normalize the distance for brightness
            brightness = np.clip(int((1 - (distance / 200)) * 100), 0, 100)

            # Set screen brightness
            sbc.set_brightness(brightness)

            # Display brightness value on the frame
            cv2.putText(frame, f"Brightness: {brightness}%", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Tracking - Brightness Control", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
