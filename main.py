import mediapipe as mp
import poseEstimation as pe 
import cv2
poseDetector=pe.poseTrack()
cap=cv2.VideoCapture(0)

while True:
    status,frame=cap.read()
    cv2.imshow("AI_Trainer",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cv2.destroyAllWindows()
cap.release()