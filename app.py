from flask import Flask, Response
import json
#from flask.wrappers import Request
#from flask_restful import Resource, Api
#from detect import video_detect
from flask import request
from flask import after_this_request
import cv2
import time
import re
from datetime import datetime
import pafy

app = Flask(__name__)
#api = Api(app)

def video_detect(ip):
    temp = ip
    try:
        print('playing',ip)
        if 'youtube.com/' in ip or 'youtu.be/' in ip:  # if source is YouTube video
            
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


#api.add_resource(Quotes, '/')
@app.route('/video', methods=['GET'])
def name():
#def catch_all(path):
    ip = request.args.get('ip')
    #print("here"+ip)
    #return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
    validjson = video_detect(ip)
    js = json.dumps(validjson)
    return Response(response=js,status=200, mimetype='application/json',headers={'Access-Control-Allow-Origin':'*'})


@app.route('/', methods=['GET'])
def name():
    return Response("<h1>Flask</h1><p>You visited: to my website</p>", mimetype="text/html")
   
if __name__ == '__main__':
    #username = request.args.get('username')
    #app.run(debug=True,host="192.168.29.63")
    app.run()
