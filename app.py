from flask import Flask, request, Response, redirect
import base64
import jsonpickle
from datetime import datetime
from dateExt import dateExtractor
from textExt import TesseractTxtExtractor
from preProc import preProcessor
import pandas as pd 
import os 
from PIL import Image
import cv2 as cv

app = Flask(__name__)
pp = preProcessor()
tx = TesseractTxtExtractor()
dx = dateExtractor()

@app.route("/extract_date", methods=['GET','POST'])
def index():
    if request.method == "POST":
        try:

            r = request
            # if r.method=="POST":
            image_64_decode = base64.decodestring(r.data)
            image_result = open('recieved_img.jpeg', 'wb')
            image_result.write(image_64_decode)
            mtx = cv.imread('recieved_img.jpeg')
            mtx = pp.rescale(mtx)
            content = tx.extractTxt(mtx)
            date = dx.extractDate(content)
            response = {'date' : date }
            # encode response using jsonpickle
            response_pickled = jsonpickle.encode(response)

        except Exception as e:
            response = {'date': 'null'}
            response_pickled = jsonpickle.encode(response)
            return Response(response=response_pickled, status=200, mimetype="application/json")    
        # print(r.data)
        
    elif request.method=="GET":
        response_pickled = "Make a POST request and see the result on your console"

    return Response(response=response_pickled, status=200, mimetype="application/json")
        
    # else:
    #     return Response(response="No Data", status=200, mimetype="application/json")
    

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")
