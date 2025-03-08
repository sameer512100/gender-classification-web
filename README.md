# Gender Classification Web Application

This web application is designed to predict the gender of a person from an uploaded facial image. It is built using the Flask web framework in Python, along with TensorFlow/Keras for the machine learning model.

## Installation

To get started, first clone the repository using the following command: `git clone [https://github.com/sameer512100/gender-classification-web.git](https://github.com/sameer512100/gender-classification-web.git)`. Next, navigate to the project directory using `cd gender-classification-web`. It's highly recommended to create and activate a virtual environment to manage dependencies: `python3 -m venv venv` followed by `source venv/bin/activate` on macOS/Linux or `venv\Scripts\activate` on Windows. Install the necessary dependencies listed in `requirements.txt` by running `pip install -r requirements.txt`. You will need to provide your own `gender_classification_model.h5` file and place it in the root directory of the project, which is the same directory as `app.py`. Finally, run the Flask application using `python app.py` and open your web browser to `http://127.0.0.1:5000/`.

## Usage

To use the application, simply upload an image of a person's face by clicking the "Choose File" button. After selecting the image, click the "Predict" button. The predicted gender, either "Male" or "Female", will be displayed below the button.

## Dependencies

This project relies on the following Python libraries: Flask for the web framework, TensorFlow/Keras for the machine learning model, and Pillow (PIL) for image processing.

## Model Information

The gender classification model is a Convolutional Neural Network (CNN) trained on facial images resized to 150x150 pixels. It outputs a probability, which is then converted to "Male" or "Female" based on a 0.5 threshold. Note that the `gender_classification_model.h5` file is not included in this repository due to its large size. You must provide your own model file.

## Author

This application was created by Sameer Sayyed.

## Notes

The accuracy of the model is dependent on the quality and characteristics of the input image. This application is intended for demonstration purposes.
