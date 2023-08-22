
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model

#gdown code from here( was a seperate script before)
import gdown

file_id = "https://drive.google.com/file/d/1-Ba3UlzLKhtOGuffVbxVPBiymaPd8hYH/view?usp=sharing"
output_file = "reuben_model_innception.h5"

gdown.download(file_id, output_file, quiet=False, fuzzy=True)
#till here

app = Flask(__name__)
model = keras.models.load_model('reuben_model_innception.h5')

def preprocess_image(image):
    image = image.resize((299, 299))  #inception model expected input
    image = image.convert('RGB')  # Convert grayscale to RGB
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def classify_image(image):
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)
    print (predictions)
    return predictions
    

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if 'image' not in request.files:
        return "No image uploaded"
    image = request.files['image']
    image = Image.open(image)
    predictions = classify_image(image)
    predicted_class = np.argmax(predictions[0])
    
    loss=(predictions[0][1])
    accuracy=round((predictions[0][0])*100,2)
    message="maybe your image is invalid"
    print(accuracy)
    print(loss)
    
    if predicted_class == 0:
    
        return render_template('covid.html',accuracy=accuracy,loss=loss)
    else:
        return render_template('negative.html',accuracy=accuracy,loss=loss)



if __name__ == '__main__':
    app.run()
