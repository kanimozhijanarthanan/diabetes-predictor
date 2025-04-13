from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])[0]
    result = '🟢 Not Diabetic' if prediction == 0 else '🔴 Diabetic'
    return render_template('index.html', prediction=result)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=10000)