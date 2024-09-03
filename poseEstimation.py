import mediapipe as mp
import cv2
import numpy as np
import time
import math
class poseTrack():
    def __init__(self,mode=False, upBody=False, smooth=True, detectionConf=0.5,trackConf=0.5):
        self.mode=mode
        self.upBody=upBody
        self.smooth=smooth
        self.detectionConf=detectionConf
        self.trackConf=trackConf
        
        self.mpPose=mp.solutions.pose
        self.pose= self.mpPose.Pose()
        self.mpDraw=mp.solutions.drawing_utils
        
    def poseDetector(self,frame,Draw=True):
        
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.results=self.pose.process(frameRGB)
        
        if self.results.pose_landmarks:
            if Draw:
                self.mpDraw.draw_landmarks(frame,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
             
        return frame
    def posePosition(self,frame,Draw=False):
        
        self.lmList=[]
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c=frame.shape
                px, py = int(lm.x*w) , int(lm.y*h)
                self.lmList.append([id,px,py])
                if Draw:
                    cv2.circle(frame,(px,py),10,(255,0,0),3)
        return self.lmList
    
    def findAngle(self,frame,p1,p2,p3,draw=True):
        
        x1,y1 = self.lmList[p1][1:]
        x2,y2 = self.lmList[p2][1:]
        x3,y3 = self.lmList[p3][1:]
        
        angle = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))
        if angle < 0:
            angle += 360
            
        #cv2.putText(frame,text=str(int(angle)),org=(x2+10,y2+10),color=(255,0,0),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,thickness=2)
        
        if draw:
            cv2.circle(frame,center=(x1,y1),radius=15,color=(0,0,255),thickness=1)
            cv2.circle(frame,center=(x1,y1),radius=5,color=(0,0,255),thickness=-1)
            cv2.line(frame,pt1=(x1,y1),pt2=(x2,y2),color=(255,255,255),thickness=2)
            
            cv2.circle(frame,center=(x2,y2),radius=15,color=(0,0,255),thickness=1)
            cv2.circle(frame,center=(x2,y2),radius=5,color=(0,0,255),thickness=-1)
            cv2.line(frame,pt1=(x3,y3),pt2=(x2,y2),color=(255,255,255),thickness=2)
            
            cv2.circle(frame,center=(x3,y3),radius=15,color=(0,0,255),thickness=1)
            cv2.circle(frame,center=(x3,y3),radius=5,color=(0,0,255),thickness=-1)
            
        return frame,angle
def main():
    pass
    

if __name__ == '__main__':
    main()