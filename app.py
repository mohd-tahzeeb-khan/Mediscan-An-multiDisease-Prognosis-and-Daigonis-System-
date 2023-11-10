from flask import Flask, render_template, request, flash
import numpy as np
import os
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.models import load_model
uploadedimges='static/userUpload'


#loading models
#heart_model=load_model("")
#daibeties_model=load_model("models\diabetes_model.pkl")
lungs_model=load_model("models\Lungs_disease.h5")
skin_model=load_model("models\Skin_disease4.h5")
brain_model=load_model("models\brain_disease.h5")
print("models loaded")
def brain_models_prediction(brain_Images):
    test_image=load_img(brain_Images, target_size=(224, 224))
    test_image = img_to_array(test_image)/255 # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
    result = brain_model.predict(test_image).round(3) # predict diseased palnt or not
    print('@@ Raw result = ', result)
    pred=np.argmax(result)
    if pred == 0:
        return 'Glioma', 'diganosis.html' # if index 0 burned leaf
    elif pred==1:
        return 'Menigioma', 'index.html'
    elif pred==2:
        return "NO Tumor", 'index.html'
#-----------------------------------------------------------------------------------------------------------------    
def lungs_models_prediction(lungs_Images):
    test_image=load_img(kungs_Images, target_size=(224, 224))
    test_image = img_to_array(test_image)/255 # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
    result = brain_model.predict(test_image).round(3) # predict diseased palnt or not
    print('@@ Raw result = ', result)
    pred=np.argmax(result)
    if pred == 0:
        return 'Bacterial Pneumonia', 'diganosis.html' # if index 0 burned leaf
    elif pred==1:
        return 'Normal', 'index.html'
    elif pred==2:
        return "Tuberculosis", 'index.html'
    elif pred==3:
        return "Viral Pneumonia", 'index.html'
#----------------------------------------------------------------------------------------------------------
def skin_models_prediction(skin_Images):
    test_image=load_img(skin_Images, target_size=(224, 224))
    test_image = img_to_array(test_image)/255 # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
    result = brain_model.predict(test_image).round(3) # predict diseased palnt or not
    print('@@ Raw result = ', result)
    pred=np.argmax(result)
    if pred == 0:
        return 'Acne', 'diganosis.html' # if index 0 burned leaf
    elif pred==1:
        return 'Normal', 'index.html'
    elif pred==2:
        return "Vascular Tumors", 'index.html'
    elif pred==3:
        return "Fungal", 'index.html'
#------------------------------------------------------------------------------------------------------------
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
    return render_template("upload.html")
@app.route("/predict-brain", methods=['POST'])
def predict_Brain():
    if request.method=='POST':
        file=request.files['image']
        filename=file.filename
        if filename=="":
            flash("Please Insert a Images", "error")
            return render_template('index.html')
        file_path = os.path.join(uploadedimges, filename)
        file.save(file_path)
        pred, output_page=brain_models_prediction(brain_Images=file_path)
        return render_template(output_page, pred_output=pred, user_image=file_path)


if __name__=="__main__":
    app.run(debug=True)