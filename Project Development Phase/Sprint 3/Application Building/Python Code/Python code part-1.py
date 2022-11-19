from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf
from flask import Flask
#You need to use following line [app Flask(__name__]
app = Flask(__name__,template_folder="templates")
model = load_model("models\mnistCNN.h5")


@app.route('/')
def upload_file():
  return render_template('main.html')
@app.route('/main')
def upload_file1():
  return render_template('index.html')
@app.route('/predict',methods = ['POST'])
def upload_image_file():
  if request.method == 'POST':
    img = Image.open(request.files['file'].stream).convert("L")
    img = img.resize((28,28))
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1,28,28,1)
    y_pred = model.predict_classes(im2arr)
    print(y_pred) 