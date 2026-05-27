# 🎓 Student Performance & Placement Predictor (ML Web App)

## 🚀 Overview
This is a Machine Learning web application built using Python and Streamlit that predicts student academic performance and placement outcomes based on input features like study hours, attendance, CGPA, and previous marks.

The project demonstrates an end-to-end ML pipeline including data processing, model training, prediction, and a web interface.

---

## 🎯 Features (Current Version)
- 📊 Predicts student exam score using Linear Regression
- ✅ Predicts Pass / Fail using Logistic Regression
- 🏢 Predicts Placement using Random Forest Classifier
- 🌐 Interactive web UI using Streamlit
- ⚡ Real-time predictions based on user input

---

## 🧠 Machine Learning Models Used
- Linear Regression → Score Prediction
- Logistic Regression → Pass / Fail Classification
- Random Forest → Placement Prediction

---

## 📂 Project Structure
student-ml-app/
│
├── app.py              # Streamlit frontend UI
├── model.py            # ML training and prediction logic
├── utils.py            # Helper functions (preprocessing)
├── data.csv            # Dataset used for training
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

---

## ⚙️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## 📊 How It Works
1. User enters student details (study hours, attendance, CGPA, previous marks)
2. Data is passed to trained ML models
3. Models generate predictions:
   - Score prediction
   - Pass/Fail classification
   - Placement prediction
4. Results are displayed in a Streamlit web interface

---

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
