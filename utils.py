import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def scale_data(df):
	scaler=MinMaxScaler()
	cols=["study_hours","attendance","cgpa","previous_marks"]
	df[cols]=scaler.fit_transform(df[cols])
	return df,scaler

def format_input(study_hours, attendance, cgpa, previous_marks): 
	return [[study_hours, attendance, cgpa, previous_marks]]


"""
🔴 Problem without scaling:

Your data looks like:

feature	range
study_hours	1–10
attendance	0–100
cgpa	0–10

👉 ML gets confused because values are in different ranges.

🟢 What scaling does:

It converts everything into:

0 → 1 range

Example:

original	scaled
10 hours	0.9
5 hours	0.4
1 hour	0.1
"""