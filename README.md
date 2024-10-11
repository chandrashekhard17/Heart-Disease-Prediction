# ❤️ Heart Disease Prediction using Machine Learning

![Heart Disease Prediction](https://img.shields.io/badge/Heart%20Disease%20Prediction-Machine%20Learning-brightgreen)  
Predict heart disease with high accuracy using the **RandomForestClassifier** model! This project leverages medical data to predict whether a person is at risk of heart disease, offering an easy-to-use web interface powered by Flask.  

---

## 🚀 **Project Overview**

Heart disease is one of the leading causes of death worldwide. Early prediction and diagnosis are crucial for improving treatment and preventing fatalities. This project aims to predict heart disease using a **Random Forest** machine learning model, built on medical records like blood pressure, cholesterol levels, and other vital statistics.

This project includes:
- **Machine Learning-based Predictions**: Using RandomForestClassifier.
- **Interactive Web Application**: A user-friendly Flask app for real-time heart disease risk assessment.
- **Data Visualization**: Explore important factors contributing to heart disease through visualizations.

---

## 🔑 **Key Features**
- **Highly Accurate Predictions**: RandomForestClassifier is used to ensure reliable results.
- **Interactive Web Interface**: Predict heart disease risk based on real-time user inputs.
- **Health Insights**: Learn more about key health factors impacting heart disease risk through interactive charts and graphs.

---

## 🛠 **Technologies Used**
- **Python** 🐍: The core programming language for the model and Flask app.
- **Scikit-learn**: For building and training the Random Forest model.
- **Flask** 🌐: For creating a user-friendly web interface.
- **Pandas**: For data manipulation and preprocessing.
- **HTML/CSS**: For designing the web application.
- **Matplotlib/Seaborn** 📊: For data visualization.

---

## ⚙️ **How to Get Started**

### Prerequisites
- Python 3.x installed
- Libraries: Flask, Scikit-learn, Pandas, Matplotlib, Seaborn, etc.

### Step-by-Step Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/chandrashekhard17/Heart-Disease-Prediction.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd heart-disease-prediction
    ```

3. **Install Required Libraries**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```bash
    python app.py
    ```

5. **Access the App**:
    Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## 🧠 **How It Works**

1. **Input**: Users provide basic health information such as age, cholesterol, and blood pressure.
2. **Processing**: The data is processed through a trained **RandomForestClassifier** model.
3. **Prediction**: The model predicts the likelihood of heart disease and presents the result to the user.
4. **Visual Feedback**: Visualizations of important health metrics provide insights into what factors are contributing to the prediction.

---

## 🎯 **Model Performance**

The **RandomForestClassifier** was selected due to its robust performance and ability to handle complex datasets.

| Metric       | Score     |
|--------------|-----------|
| **Accuracy** | 87%       |
| **Precision**| 85%       |
| **Recall**   | 85%       |
| **F1-Score** | 85%       |

*RandomForestClassifier* has proven to be highly effective in predicting heart disease by analyzing diverse health data.

---

## 📊 **Data Visualizations**

The app includes insightful data visualizations to help users understand key factors:
- **Age Distribution**: How age affects heart disease likelihood.
- **Cholesterol Levels**: The impact of cholesterol on heart disease risk.
- **Blood Pressure Insights**: How blood pressure correlates with the prediction.

---

## 🌐 **Demo**

Here’s a quick look at how the web app works:

![App Demo](app_demo.gif)  
*Provide a GIF or image of your app interface in action here.*

---

## 👩‍💻 **Contributing**

Want to contribute to this project? Here’s how you can help:
1. Fork the repo and create a new branch (`git checkout -b feature-branch`).
2. Make your changes and commit (`git commit -m 'Add awesome feature'`).
3. Push to your branch (`git push origin feature-branch`).
4. Open a pull request, and I’ll review your changes!

---


## 👏 **Acknowledgments**

Special thanks to:
- The creators of the UCI Heart Disease Dataset.

