import numpy as np
import PIL
from keras.models import load_model
from flask import Flask, render_template
from flask import request
import cv2	


model = load_model('my_model.hdf5')
app = Flask(__name__)

def predict_label(img_path, model):
    image=cv2.imread(img_path)
    image_resized= cv2.resize(image, (75,75))
    image=np.expand_dims(image_resized,axis=0)
    pred=model.predict(image)
    class_names = ['Bed', 'Chair', 'Sofa']
    output_class=class_names[np.argmax(pred)]
    return output_class

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/submit", methods = ['GET', 'POST'])
def get_hours():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save(img_path)
        p = predict_label(img_path,model)
        
    return render_template("index.html", prediction = p, img_path = img_path)

if __name__ == '__main__':
      app.run(debug=True,use_reloader=False)