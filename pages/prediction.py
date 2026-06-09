import streamlit as st
import pandas as pd
import joblib

st.title("🔮 Customer Churn Prediction")

try:
    model = joblib.load("models/churn_model.pkl")

    st.subheader("Enter Customer Details")

    income = st.number_input(
        "Income",
        min_value=1000,
        max_value=500000,
        value=50000
    )

    spending_score = st.slider(
        "Spending Score",
        1,
        100,
        50
    )

    tenure = st.slider(
        "Tenure (Months)",
        1,
        60,
        12
    )

    if st.button("Predict Churn"):

        input_data = pd.DataFrame(
            [[income, spending_score, tenure]],
            columns=[
                "income",
                "spending_score",
                "tenure"
            ]
        )

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]

        if prediction == 1:
            st.error("⚠ High Risk Customer (Likely to Churn)")
        else:
            st.success("✅ Customer Likely to Stay")

        st.subheader("Prediction Probability")

        st.write(
            f"Stay Probability: {probability[0]*100:.2f}%"
        )

        st.write(
            f"Churn Probability: {probability[1]*100:.2f}%"
        )

except Exception as e:
    st.error(
        "Model not found. Please train the model first."
    )