import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Customer Recommendation Engine", layout="wide")

st.title("🎯 AI Customer Recommendation System")

# Load dataset
df = pd.read_csv("data/customers.csv")

# -------------------------------
# SELECT CUSTOMER
# -------------------------------
st.subheader("📌 Select Customer")

customer_id = st.selectbox(
    "Choose Customer ID",
    df["customer_id"]
)

customer = df[df["customer_id"] == customer_id].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.write("**Name:**", customer["name"])
    st.write("**City:**", customer["city"])
    st.write("**Income:**", customer["income"])

with col2:
    st.write("**Favorite Product:**", customer["favorite_product"])
    st.write("**Category:**", customer["favorite_category"])
    st.write("**Spending Score:**", customer["spending_score"])

st.markdown("---")

# -------------------------------
# PRODUCT RECOMMENDATIONS
# -------------------------------
st.subheader("🛍 Product Recommendations")

similar_products = df[
    df["favorite_category"] == customer["favorite_category"]
]["favorite_product"].unique()

recommended = [p for p in similar_products if p != customer["favorite_product"]]

if recommended:
    for item in recommended[:5]:
        st.success(item)
else:
    st.info("No additional recommendations available.")

st.markdown("---")

# -------------------------------
# SIMILAR CUSTOMERS
# -------------------------------
st.subheader("👥 Similar Customers")

similar_customers = df[
    (df["income"].between(customer["income"] - 10000, customer["income"] + 10000)) &
    (df["customer_id"] != customer_id)
]

st.dataframe(
    similar_customers[[
        "customer_id",
        "name",
        "city",
        "income",
        "favorite_product"
    ]].head(10),
    use_container_width=True
)

st.markdown("---")

# -------------------------------
# AI STYLE FILTER (OPTIONAL)
# -------------------------------
st.subheader("🤖 AI Recommendation Filter")

age = st.number_input("Age", min_value=18, max_value=80, value=25)
income_input = st.number_input("Annual Income", min_value=10000, max_value=200000, value=50000)

if st.button("Get Recommendations"):

    filtered = df[
        (df["income"].between(income_input - 15000, income_input + 15000))
    ]

    st.subheader("👥 Similar Customers")

    if len(filtered) > 0:
        st.dataframe(
            filtered[[
                "customer_id",
                "name",
                "age",
                "income",
                "city",
                "favorite_product"
            ]].head(10),
            use_container_width=True
        )

        st.subheader("🛍 Recommended Products")

        recommendations = filtered["favorite_product"].value_counts().index.tolist()

        for product in recommendations[:5]:
            st.success(product)

        st.info(f"Found {len(filtered)} similar customers.")

    else:
        st.warning("No similar customers found. Try different values.")