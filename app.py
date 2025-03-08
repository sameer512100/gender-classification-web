from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

try:
    model = tf.keras.models.load_model('gender_classification_model.h5')
    if model is not None:
        print(f"Model loaded. Input shape: {model.input_shape}")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def preprocess_image(image_bytes):
    try:
        print("Starting preprocess_image")
        img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        print("Image opened successfully")
        print(f"Original image size: {img.size}")

        expected_width = 150  # Correct width
        expected_height = 150 # Correct height

        img = img.resize((expected_width, expected_height))
        print(f"Image resized to: {img.size}")
        img_array = np.array(img) / 255.0
        print("Image array created and normalized")
        img_array = np.expand_dims(img_array, axis=0)
        print("Batch dimension added")
        return img_array
    except Exception as e:
        print(f"Image processing error: {e}")
        return None

def predict_gender(image_bytes):
    if model is None:
        return "Model loading error"
    processed_image = preprocess_image(image_bytes)
    if processed_image is None:
        return "Image processing failed"
    try:
        print(f"Processed image shape: {processed_image.shape}")
        prediction = model.predict(processed_image)
        print(f"Raw prediction: {prediction}")

        if prediction[0][0] > 0.5:
            return "Female"
        else:
            return "Male"
    except Exception as e:
        print(f"Prediction error: {e}")
        return f"Prediction error: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'})
        image = request.files['image'].read()
        prediction = predict_gender(image)
        return jsonify({'prediction': prediction})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)