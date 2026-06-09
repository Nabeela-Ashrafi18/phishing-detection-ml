from pyexpat import features

from flask import Flask, render_template, request
import joblib
from feature_extraction import extract_features

app = Flask(__name__)

model = joblib.load('phishing_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():

    prediction = ""

    if request.method == 'POST':

        url = request.form['url']

        features = [extract_features(url)]
        result = model.predict(features)
        prob = model.predict_proba(features)
        print("Prediction:", result)
        print("Probability:", prob) 
        
        if result[0] == 0:
            prediction = "🟢 Safe Website"
        else:
            prediction = "🔴 Potentially Malicious Website"

    return render_template('index.html',
                           prediction=prediction)

app.run(debug=True)
features = [extract_features(url)]
result = model.predict(features)