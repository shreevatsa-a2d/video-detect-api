from flask import Flask, Response
import json
#from flask.wrappers import Request
#from flask_restful import Resource, Api
from detect import video_detect
from flask import request
from flask import after_this_request

app = Flask(__name__)
#api = Api(app)


#api.add_resource(Quotes, '/')
@app.route('/', methods=['GET'])
def name():
#def catch_all(path):
    ip = request.args.get('ip')
    #print("here"+ip)
    #return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
    validjson = video_detect(ip)
    js = json.dumps(validjson)
    return Response(response=js,status=200, mimetype='application/json',headers={'Access-Control-Allow-Origin':'*'})


if __name__ == '__main__':
    #username = request.args.get('username')
    #app.run(debug=True,host="192.168.29.63")
    app.run(debug=True)