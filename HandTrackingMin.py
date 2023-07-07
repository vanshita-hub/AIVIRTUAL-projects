import cv2
import img as img
import mediapipe as mp

cap = cv2.VideoCapture(0)


while True:
    success, imp = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(0)
