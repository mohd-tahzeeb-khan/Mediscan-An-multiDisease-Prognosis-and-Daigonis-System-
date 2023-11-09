from flask import Flask, render_template, request, flash
import flask
import numpy as np
import os
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.models import load_model

#loading models
#heart_model=load_model("")
#daibeties_model=load_model("models\diabetes_model.pkl")
#lungs_model=load_model("models\Lungs_disease.h5")
#skin_model=load_model("models\Skin_disease4.h5")
#brain_model=load_model("models\brain_disease.h5")
print("models loaded")
class predict:
    def __init__():#init function
        pass
app=Flask(__name__)
app.secret_key="secret key"
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")
@app.route("/diagnosis", methods=['GET'])
def diagnosis():
    return render_template("diganosis.html")
@app.route("/diabetes", methods=['GET','POST'])
def diabetes():
    return render_template("diabetesform.html")
@app.route("/credits", methods=["GET"])
def credits():
    return render_template("credit.html")
@app.route("/about", methods=["GET"])
def help():
    return render_template("help.html")


if __name__=="__main__":
    app.run(threaded=True)