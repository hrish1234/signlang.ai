from flask import Flask, render_template, request, jsonify
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
app = Flask(__name__)

@app.route('/')
def home():
       return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
       data = request.get_json(force=True)
       features = np.asarray(data['features']).reshape(1, -1)

       prediction = model.predict(features)[0]
       return jsonify({'prediction': prediction})

if __name__ == '__main__':
       app.run(debug=True)
   

