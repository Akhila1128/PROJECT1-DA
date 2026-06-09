import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# ==========================
# TITLE
# ==========================
st.title("⚠ AI Customer Churn Prediction System")

# ==========================
# LOAD DATA
# ==========================
df = pd.read_csv("data/customers.csv")

# ==========================
# FEATURE SELECTION
# ==========================
features = ["income", "spending_score", "tenure"]

df = df.dropna()

X = df[features]
y = df["churn"]

# ==========================
# TRAIN MODEL
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

st.success(f"Model Accuracy: {round(accuracy * 100, 2)}%")

st.markdown("---")

# ==========================
# USER INPUT
# ==========================
st.subheader("📌 Predict Customer Churn")

income = st.number_input("Income", 10000, 200000, 50000)
spending_score = st.number_input("Spending Score", 0, 100, 50)
tenure = st.number_input("Tenure (months)", 1, 120, 12)

if st.button("Predict Churn"):

    input_data = pd.DataFrame([[
        income,
        spending_score,
        tenure
    ]], columns=features)

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠ Customer will CHURN (Risk: {round(probability*100,2)}%)")
    else:
        st.success(f"✅ Customer will STAY (Risk: {round(probability*100,2)}%)")

st.markdown("---")

# ==========================
# VISUAL ANALYSIS
# ==========================
st.subheader("📊 Churn Distribution")

fig1 = px.pie(
    values=df["churn"].value_counts().values,
    names=["Stay", "Churn"]
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("📉 Spending vs Churn")

fig2 = px.box(
    df,
    x="churn",
    y="spending_score",
    color="churn"
)

st.plotly_chart(fig2, use_container_width=True)

# ==========================
# HIGH RISK CUSTOMERS
# ==========================
st.subheader("🚨 High Risk Customers")

risk_customers = df[
    (df["tenure"] < 12) &
    (df["spending_score"] < 40)
]

st.dataframe(
    risk_customers[[
        "customer_id",
        "name",
        "income",
        "spending_score",
        "tenure"
    ]],
    use_container_width=True
)