from flask import Flask, render_template, request, flash
import flask
import numpy as np
import os
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.models import load_model

#loading models
heart_model=load_model("")
daibeties_model=load_model("")
lungs_model=load_model("")
skin_model=load_model("")
brain_model=load_model("")

class predict:
    def __init__():
        pass
app=Flask(__name__)
app.secret_key="secret key"
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")
@app.route("/credits", methods=["GET"])
def credits():
    return render_template("credits.html")
@app.route("/help", methods=["GET"])
def help():
    return render_template("help.html")

if __name__=="__main__":
    app.run(threaded=True)