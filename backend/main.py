from flask import Flask, request, jsonify

# from keras.models import load_model
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load your pre-trained Keras model (make sure to adjust the model filename and path)
# model = load_model('your_model.h5')  # Replace 'your_model.h5' with the actual filename of your model


# Define a route for the API to make predictions
@app.route("/predict", methods=["POST"])
def predict():
    # try:
    #     # Get the data from the POST request
    #     data = request.get_json(force=True)

    #     # Assuming your model expects a feature vector
    #     features = np.array(data['features'])  # Ensure features is a list or array

    #     # If your model expects a specific shape, reshape it as required
    #     # For example, if the model expects a 2D array: features = features.reshape(1, -1)
    #     features = features.reshape(1, -1)  # Modify this as per your model's input shape

    #     # Predict the result using the Keras model
    #     prediction = model.predict(features)

    #     # Return the prediction result as JSON
    #     return jsonify({'prediction': prediction.tolist()})
    # except Exception as e:
    #     return jsonify({'error': str(e)}

    return "Predict test"


# Define the main route
@app.route("/home")
def home():
    return "Welcome to the Keras model API!"


@app.route("/getSomething")
def getSomething():
    return "Take something from me, testt"


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
