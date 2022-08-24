from flask import Flask, render_template , request , jsonify
from PIL import Image
import os , io , sys
import numpy as np 
import cv2
import base64
import torch
import shutil

app = Flask(__name__)

@app.route('/detectObject' , methods=['POST'])
def mask_image():

    file = request.files['image'].read()
    img = Image.open(io.BytesIO(file))

    results = model(img, size=640)
    results.render()

    path = "D:/yolov5/web_app/runs/detect/"
    shutil.rmtree(path)

    results.save()

    img_path = 'D:/yolov5/web_app/runs/detect/exp/image0.jpg'
    rawBytes = io.BytesIO()

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img.save(rawBytes, format="JPEG")

    rawBytes.seek(0)
    img_base64 = base64.b64encode(rawBytes.read())

    return jsonify({'status':str(img_base64)})

@app.route('/test' , methods=['GET','POST'])
def test():
    print("log: got at test" , file=sys.stderr)
    return jsonify({'status':'succces'})

@app.route('/')
def home():
    return render_template('./index.html')


@app.after_request
def after_request(response):
    print("log: setting cors" , file = sys.stderr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    # model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True, autoshape=True)  
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/yolov5/web_app/best.pt')
    model.eval()
    app.run(debug = True)
    app.run(host="0.0.0.0", port=args.port) 

