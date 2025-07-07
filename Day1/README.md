# 🚢 Titanic Survival Prediction

This project is part of my 30 Days 30 Project Challenge. It predicts the survival of passengers on the Titanic using machine learning models trained on the famous Titanic dataset.

Demo Video:- 
<video controls src="20250707-0441-36.2664777.mp4" title="Titanic"></video>

## 📌 What it does
- Takes passenger information (class, age, sex, fare, etc.)
- Predicts whether the passenger would have survived the Titanic disaster
- Provides a web interface built with Flask for easy input and results

## 📂 Key files
- `app.py`: Flask backend serving the prediction model
- `titanic_model.pkl`: Serialized machine learning model trained on Titanic data
- `templates/`: HTML templates for the web interface
- `static/`: CSS styles and Titanic-themed images
- `Titanic Survival Prediction.ipynb`: Jupyter notebook used for data preprocessing, model training, and evaluation

## 💡 Technologies used
- Python (Pandas, scikit-learn, NumPy)
- Flask
- HTML, CSS
- Git for version control

## 🚀 How to run locally
1. Clone the repository:
   ```bash
   git clone https://github.com/omkarbandikatte/30Days30ProjectChallenge.git
   cd 30Days30ProjectChallenge/Day1

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Start the Flask app:
    ```bash
    python app.py