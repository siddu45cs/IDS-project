from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained NIDS model
model = joblib.load("models/nids_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    if file:
        try:
            # Read uploaded CSV file
            data = pd.read_csv(file, engine="python")

            # Make predictions for all rows
            predictions = model.predict(data)

            # Calculate statistics
            total = len(predictions)
            normal = list(predictions).count("BENIGN")
            malicious = total - normal

            return render_template(
                "index.html",
                prediction_text=f"""
                Total Records Analyzed: {total} <br>
                Normal Traffic: {normal} <br>
                Malicious Traffic: {malicious}
                """
            )

        except Exception as e:
            return render_template(
                "index.html",
                prediction_text=f"Error: {str(e)}"
            )

    return render_template("index.html", prediction_text="No file uploaded")

if __name__ == "__main__":
    app.run(debug=True)