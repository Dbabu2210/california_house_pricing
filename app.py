import pandas as pd
import numpy as np
import pickle
from flask import render_template, jsonify, Flask, request

app = Flask(__name__)
reg_model = pickle.load(open('regression.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))
@app.route('/')
def home():
    return "Hello"
@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = reg_model.predict(new_data)
    print(output[0])
    return jsonify(output[0])
    
if __name__ == '__main__':
    app.run(debug=True)