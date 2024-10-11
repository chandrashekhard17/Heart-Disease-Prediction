from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)


try:
    model = pickle.load(open('models/model.pkl', 'rb'))
    scaler = pickle.load(open('models/scaler.pkl', 'rb'))
except Exception as e:
    raise RuntimeError("Failed to load model or scaler: " + str(e))

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict heart disease based on user input."""
    try:
        
        input_data = [
            float(request.form.get('age', 0)),
            float(request.form.get('sex', 0)),
            float(request.form.get('cp', 0)),
            float(request.form.get('trestbps', 0)),
            float(request.form.get('chol', 0)),
            float(request.form.get('fbs', 0)),
            float(request.form.get('restecg', 0)),
            float(request.form.get('thalach', 0)),
            float(request.form.get('exang', 0)),
            float(request.form.get('oldpeak', 0)),
            float(request.form.get('slope', 0)),
            float(request.form.get('ca', 0)),
            float(request.form.get('thal', 0))
        ]

       
        input_data_df = pd.DataFrame([input_data], columns=[
            'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
            'restecg', 'thalach', 'exang', 'oldpeak', 
            'slope', 'ca', 'thal'
        ])

        
        input_data_scaled = scaler.transform(input_data_df)

       
        prediction = model.predict(input_data_scaled)
        probability = model.predict_proba(input_data_scaled)[:, 1]

        
        result_message = (
            "Patient is predicted to have heart disease." if prediction[0] == 1 
            else "Patient is predicted to be free of heart disease."
        )

        
        return render_template(
            'result.html',
            prediction=result_message,
            probability=round(probability[0] * 100, 2)
        )

    except ValueError as ve:
        return render_template('error.html', error_message=f"Input Error: {ve}")
    except Exception as e:
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
