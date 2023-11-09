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
def lungs_models_prediction(images):
    test_image=load_img(images, target_size=(150, 150))
    test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
  result = model.predict(test_image).round(3) # predict diseased palnt or not
  print('@@ Raw result = ', result)
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
@app.route("/predict/lungs", mehtods=['POST'])
def predict_lungs():
    file=request.files['image']
    filename=file.filename
    if filename=="":
        flash("Please Insert a Images", "error")
        return render_template('index.html')
    file_path = os.path.join('static/user uploaded', filename)
    file.save(file_path)
    pred, output_page=lungs_models_prediction(lungsImages=file_path)
    return render_template(output_page, pred_output=pred, user_image=file_path)


if __name__=="__main__":
    app.run(threaded=True)