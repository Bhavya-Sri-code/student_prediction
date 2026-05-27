import streamlit as st
from model import train_models, predict, load_data

# Load data and train model
data = load_data()
models = train_models(data)

st.title("🎓 Student Performance & Placement Predictor")
st.write("Enter student details to predict performance, pass/fail and placement")

# INPUTS (IMPORTANT - YOU WERE MISSING THIS)
study_hours = st.number_input("Study Hours")
attendance = st.number_input("Attendance")
cgpa = st.number_input("CGPA")
previous_marks = st.number_input("Previous Marks")

# BUTTON
if st.button("Predict"):

    input_data = [study_hours, attendance, cgpa, previous_marks]

    score, pass_result, placement= predict(models, input_data)

    st.subheader("📊 Results")

    st.write("🎯 Predicted Score:", round(score, 2))

    if pass_result == 1:
        st.success("✅ Pass")
    else:
        st.error("❌ Fail")

    if placement == 1:
        st.success("🏢 Placed")
    else:
        st.warning("Not Placed")