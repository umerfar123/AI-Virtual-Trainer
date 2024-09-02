import mediapipe as mp
import cv2
import numpy as np
import time

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
    def posePosition(self,frame,Draw=True):
        
        lmList=[]
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c=frame.shape
                px, py = int(lm.x*w) , int(lm.y*h)
                lmList.append([id,px,py])
                if Draw:
                    cv2.circle(frame,(px,py),10,(255,0,0),3)
        return lmList
    

def main():
    pass
    

if __name__ == '__main__':
    main()