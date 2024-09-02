import mediapipe as mp
import poseEstimation as pe 
import cv2
poseDetector=pe.poseTrack()
cap=cv2.VideoCapture('trainer\o1.mp4')

while True:
    status,frame=cap.read()
    frame=cv2.resize(frame,(720,360))
    frame=poseDetector.poseDetector(frame,Draw=False)
    lmList=poseDetector.posePosition(frame,Draw=False)
    if len(lmList) !=0:
      
        rshoulder=lmList[12][1:]
        lshoulder=lmList[11][1:]
        lelbow,lwrist = lmList[13][1:],lmList[15][1:]
        frame=poseDetector.findAngle(frame,11,13,15)
    
    
    cv2.imshow("AI_Trainer",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cv2.destroyAllWindows()
cap.release()