import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier


# ---------------- LOAD DATA ----------------
def load_data():
    df = pd.read_csv("data.csv")
    return df


# ---------------- TRAIN MODELS ----------------
def train_models(data):

    # Features
    X = data[["study_hours", "attendance", "cgpa", "previous_marks"]]

    # Targets
    y_score = data["score"]
    y_pass = data["pass_fail"]
    y_place = data["placement"]

    # ---------------- SPLIT DATA ----------------
    X_train, X_test, y_score_train, y_score_test = train_test_split(
        X, y_score, test_size=0.2, random_state=42
    )

    _, _, y_pass_train, y_pass_test = train_test_split(
        X, y_pass, test_size=0.2, random_state=42
    )

    _, _, y_place_train, y_place_test = train_test_split(
        X, y_place, test_size=0.2, random_state=42
    )

    # ---------------- MODELS ----------------

    # Score Prediction (Regression)
    score_model = LinearRegression()
    score_model.fit(X_train, y_score_train)

    # Pass / Fail (Classification)
    pass_model = LogisticRegression()
    pass_model.fit(X_train, y_pass_train)

    # Placement Prediction (Better model = Random Forest)
    place_model = RandomForestClassifier(n_estimators=100, random_state=42)
    place_model.fit(X_train, y_place_train)

    # ---------------- RETURN MODELS ----------------
    return score_model, pass_model, place_model


# ---------------- PREDICTION FUNCTION ----------------
def predict(models, input_data):

    score_model, pass_model, place_model = models

    # IMPORTANT: input must be 2D
    input_data = [input_data]

    score = score_model.predict(input_data)[0]
    pass_result = pass_model.predict(input_data)[0]
    placement = place_model.predict(input_data)[0]

    return score, pass_result, placement