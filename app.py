from flask import Flask, render_template, request, flash
import numpy as np
import os
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.models import load_model
import pickle
import sklearn
uploadedimges='static/userUpload'


#loading models
heart_model=pickle.load(open("models\Heart_Model_updated.pkl", "rb"))
diabetes_model=pickle.load(open("models\diabetes_model.pkl", "rb"))
lungs_model=load_model("models\Lungs_disease.h5")
skin_model=load_model("models\Skin_disease4.h5")
brain_model=load_model("models/brain_disease.h5")
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
    test_image=load_img(lungs_Images, target_size=(224, 224))
    test_image = img_to_array(test_image)/255 # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
    result = lungs_model.predict(test_image).round(3) # predict diseased palnt or not
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
   
    result = skin_model.predict(test_image).round(3) # predict diseased palnt or not
    print('@@ Raw result = ', result)
    pred=np.argmax(result)
    if pred == 0:
        return 'Acne', 'diganosis.html' # if index 0 burned leaf
    elif pred==1:
        return 'Normal', index
    elif pred==2:
        return "Vascular Tumors", index
    elif pred==3:
        return "Fungal",index
#------------------------------------------------------------------------------------------------------------
app=Flask(__name__)
app.secret_key="secret key"
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")
@app.route("/diganosis", methods=['GET'])
def diagnosis():
    return render_template("diganosis.html")
@app.route("/credits", methods=["GET"])
def credits():
    return render_template("credit.html")
@app.route("/help", methods=["GET"])
def help():
    return render_template("help.html")
@app.route("/upload/<disease>", methods=['GET','POST'])
def upload(disease):
    if request.method=="POST":
        if disease=="lung":
            return render_template(upload,disease=disease)
        elif disease=="brain":
            return render_template(upload, disease=disease)
        elif disease=="skin":
            return render_template(upload,disease=disease)
    return render_template("upload.html", disease=disease)
@app.route("/diabetes", methods=['GET','POST'])
def diabetes():
    if request.method=='GET':
        return render_template("diabetesform.html")
    elif request.method=='POST':
        age = request.form['age']
        hypertension= request.form['hypertension']
        hba1c = float(request.form['hba1c'])
        gendervalue = request.form['gender']
        if(gendervalue=="Female"):
            gender=0
        else:
            gender=1
        smokingHistory = request.form['smokingHistory']
        if(smokingHistory=="never"):
            smoke=4
        elif(smokingHistory=="current"):
            smoke=1
        elif(smokingHistory=="formal"):
            smoke=3
        else:
            smoke=0
        heartDisease = request.form['heartDisease']
        weight = int(request.form['weight'])
        bloodGlucose=int(request.form['bloodGlucose'])
        bmi=float(request.form['BMI'])
        to_predict = np.array([[gender, age, hypertension, heartDisease, smoke, bmi, hba1c, bloodGlucose]])
        result=diabetes_model.predict(to_predict)
        print(result)
        return render_template("diabetesform.html")

@app.route("/heart", methods=['GET','POST'])
def heart():
    if request.method=='GET':
        return render_template("heartform.html")
    elif request.method=='POST':
        data=request.form
        print(data)
        to_predict=np.array(data).reshape(918,12)
        result=diabetes_model.predict(to_predict)
        print(result)
        return render_template("heartform.html")
#-----------------------------------------------------------------------------------------------------------
@app.route("/predict/<disease>", methods=['POST'])
def predict(disease):
    if request.method=='POST':
        if disease=='lungs':
            print("lungs function is working")
            file=request.files['image']
            filename=file.filename
            if filename=="":
                flash(flash_msz, "error")
                return render_template('index.html')
            file_path = os.path.join(uploadedimges, filename)
            file.save(file_path)
            pred, output_page=lungs_models_prediction(lungs_Images=file_path)
            return render_template(output_page, pred_output=pred, user_image=file_path)
        elif disease == 'brain':
            file=request.files['image']
            filename=file.filename
            if filename=="":
                flash(flash_msz, "error")
                return render_template('index.html')
            file_path = os.path.join(uploadedimges, filename)
            file.save(file_path)
            pred, output_page=brain_models_prediction(brain_Images=file_path)
            return render_template(output_page, pred_output=pred, user_image=file_path)
        elif disease=='skin':
            file=request.files['image']
            filename=file.filename
            if filename=="":
                flash(flash_msz, "error")
                return render_template('index.html')
            file_path = os.path.join(uploadedimges, filename)
            file.save(file_path)
            pred, output_page=skin_models_prediction(skin_Images=file_path)
            return render_template(output_page, pred_output=pred, user_image=file_path)
#---------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    index='index.html'
    credit='credit.html'
    help='help.html'
    upload='upload.html'
    flash_msz="Please Enter the Images. Image is not Inserted!!"
    app.run(debug=True)