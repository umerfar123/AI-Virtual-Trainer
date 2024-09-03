import mediapipe as mp
import poseEstimation as pe 
import cv2
import numpy as np

dir,count=0,0
jcount, flag = 0,0
poseDetector=pe.poseTrack()
cap=cv2.VideoCapture('trainer\o4.mp4')
workout='jj'
while True:
    
    status,frame=cap.read()
    
    if not status:
        break
    frame=cv2.resize(frame,(720,360))
    frame=poseDetector.poseDetector(frame,Draw=True)
    lmList=poseDetector.posePosition(frame,Draw=False)
    if len(lmList) !=0:

        #pushup
        if workout=='ps':
            frame ,angle = poseDetector.findAngle(frame,11,13,15)
            per = np.interp(angle, (194,290),(0,100))
            bar = np.interp(angle,(194,290),(250,50))
            
            color=(255,0,0)
            #dumbel curl checking
            if per == 100:
                color=(0,0,255)
                if dir == 0:
                    count+=0.5
                    dir=1
            if per == 0:
                color=(0,0,255)
                if dir == 1:
                    count+=0.5
                    dir=0
            #progress bar        
            cv2.rectangle(frame,pt1=(30,250),pt2=(60,50),color=(0,255,0),thickness=2)
            cv2.rectangle(frame,pt1=(30,250),pt2=(60,int(bar)),color=color,thickness=-1)
            cv2.putText(frame,text=str(int(per)),org=(25,30),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,thickness=2,color=(255,255,0))
            
            #count
            cv2.rectangle(frame,pt1=(0,360),pt2=(100,280),color=(255,0,0),thickness=-1)
            cv2.putText(frame,org=(40,330),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,thickness=2,color=(255,255,0),text=str(int(count)))
                
        #dumpels
        if workout == 'dc':
            
            frame ,angle = poseDetector.findAngle(frame,11,13,15)
            per = np.interp(angle, (210,310),(0,100))
            bar = np.interp(angle,(210,310),(250,50))
            
            color=(255,0,0)
            #dumbel curl checking
            if per == 100:
                color=(0,0,255)
                if dir == 0:
                    count+=0.5
                    dir=1
            if per == 0:
                color=(0,0,255)
                if dir == 1:
                    count+=0.5
                    dir=0
            #progress bar       
            cv2.rectangle(frame,pt1=(30,250),pt2=(60,50),color=(0,255,0),thickness=2)
            cv2.rectangle(frame,pt1=(30,250),pt2=(60,int(bar)),color=color,thickness=-1)
            cv2.putText(frame,text=str(int(per)),org=(25,30),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,thickness=2,color=(255,255,0))
            
            #count
            cv2.rectangle(frame,pt1=(0,360),pt2=(100,280),color=(255,0,0),thickness=-1)
            cv2.putText(frame,org=(40,330),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,thickness=2,color=(255,255,0),text=str(int(count)))
        
        #Pull up
        if workout == 'pl':
            
            frame ,angle = poseDetector.findAngle(frame,11,13,15)
            per = np.interp(angle, (190,277),(0,100))
            bar = np.interp(angle,(190,277),(250,50))
            
            color=(255,0,0)
            #dumbel curl checking
            if per == 0:
                color=(0,0,255)
                if dir == 0:
                    count+=0.5
                    dir=1
            if per == 100:
                color=(0,0,255)
                if dir == 1:
                    count+=0.5
                    dir=0
            #progress bar       
            cv2.rectangle(frame,pt1=(30,250),pt2=(60,50),color=(0,255,0),thickness=2)
            cv2.rectangle(frame,pt1=(30,250),pt2=(60,int(bar)),color=color,thickness=-1)
            cv2.putText(frame,text=str(int(per)),org=(25,30),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,thickness=2,color=(255,255,0))
            
            #count
            cv2.rectangle(frame,pt1=(0,360),pt2=(100,280),color=(255,0,0),thickness=-1)
            cv2.putText(frame,org=(40,330),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,thickness=2,color=(255,255,0),text=str(int(count)))
        
        #jumping jacks
        if workout =='jj':
            
            #frame ,angle = poseDetector.findAngle(frame,11,13,15)
            
            xrh , yrh = lmList[29][1:]
            xlh , ylh = lmList[30][1:]
            
            xrw , yrw = lmList[15][1:]
            xlw , ylw = lmList[16][1:]
            #print("heel:",xrh,xlh)
            #print('wrist:',xrw,xlw)
            
            if (xrh - xlh > 40) and (xrw - xlw < 60):
                print("jacked")
                flag = 1
            else :
                print('0')
                if flag:
                    jcount += 1 
                flag=0
    
            cv2.putText(frame,text=str(jcount),color=(0,255,0),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,thickness=2,org=(20,340))
    
    cv2.imshow("AI_Trainer",frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cv2.destroyAllWindows()
cap.release()