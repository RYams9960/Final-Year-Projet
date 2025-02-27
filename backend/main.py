import os
import re
import numpy as np

from keras.models import load_model
from flask import Flask, request, redirect, url_for, render_template, session, flash

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = "This_Is_mY_SecRet_aPI-Key_For-FiNal_Year_ProjEcT"

# Load your pre-trained Keras model (make sure to adjust the model filename and path)
model = load_model("My_Computing_Project_Model.h5")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Query the database for the user
        user = User.query.filter_by(username=username).first()

        # Check if user exists and password matches
        if user and check_password_hash(user.password, password):
            session["username"] = username
            flash("Logged in successfully!")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out successfully!")
    return redirect(url_for("login"))


# Define a route for the API to make predictions
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the data from the POST request
        data = request.get_json(force=True)

        # Assuming your model expects a feature vector
        features = np.array(data["features"])  # Ensure features is a list or array

        # If your model expects a specific shape, reshape it as required
        # For example, if the model expects a 2D array: features = features.reshape(1, -1)
        features = features.reshape(
            1, -1
        )  # Modify this as per your model's input shape

        # Predict the result using the Keras model
        prediction = model.predict(features)

        # Return the prediction result as JSON
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

    return "Predict test"


@app.route("/list-files", methods=["GET"])
def list_files():
    train_path = "E:/BraTS-Dataset/filtered_data/train/images"
    val_path = "E:/BraTS-Dataset/filtered_data/val/images"

    paths = [train_path, val_path]
    all_files = []

    for path in paths:
        if not os.path.exists(path) or not os.path.isdir(path):
            return jsonify({"error": f"Invalid directory path: {path}"}), 400

        try:
            all_files.extend(os.listdir(path))
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Sort the list based on the numeric part of the filenames
    sorted_file_names = sorted(
        all_files, key=lambda x: int(re.search(r"(\d+)", x).group())
    )

    return sorted_file_names


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
