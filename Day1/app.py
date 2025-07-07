from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model
with open('titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    pclass = int(request.form['pclass'])
    sex = request.form['sex']
    age = float(request.form['age'])
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])
    fare = float(request.form['fare'])
    embarked = request.form['embarked']
    title = request.form['title']
    
    # Encode categorical variables: assuming 0=male, 1=female; C=0, Q=1, S=2; simple example
    sex_num = 1 if sex == 'male' else 0
    embarked_map = {'C':1, 'S':2, 'Q':3}
    title_map = {
        'Mr': 1, 'Mrs': 2, 'Miss': 3, 'Master': 4, 'Rare': 5
    }
    title = title_map.get(title, 5)
    embarked_num = embarked_map.get(embarked, 2)
    
    # Prepare feature vector (order must match training!)
    features = np.array([[pclass, sex_num, age, sibsp, parch, fare, embarked_num, title]], dtype=object)
    
    # Predict
    prediction = model.predict(features)[0]
    result = "Congratulation You Survived" if prediction == 1 else "Meet on Next Birth"
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
