import cv2
import time
import re
from datetime import datetime



def video_detect(ip):
    temp = ip
    try:
        print('playing',ip)
        if 'youtube.com/' in ip or 'youtu.be/' in ip:  # if source is YouTube video
            import pafy
            ip = pafy.new(ip).getbest(preftype="mp4").url  # YouTube URL
        ip = eval(ip) if ip.isnumeric() else ip
        cap = cv2.VideoCapture(ip)
        if not cap.isOpened():
            raise NameError('Camera not found')
            
        count = 0
        print ("Converting video..\n")
        while cap.isOpened():
            # Extract the frame
            try:
                ret, frame = cap.read()
                if not ret:
                    continue
                return {"valid":True,"message":"valid ip"}
            except Exception as e:
                return {"valid":False,"message":"camera not responding"}
            except :
                return {"valid":False,"message":"camera not responding"}
                
    except cv2.error as error:
        return {"valid":False,"message":"invalid ip" }
    except Exception as e:
        return {"valid":False,"message":"invalid ip"}
    except :
        return {"valid":False,"message":"invalid ip"}

#result=video_detect("https://www.youtube.com/watch?v=AdUw5RdyZx")
#result=video_detect("https://192.168.29.200:8080/video")

#print(result)
