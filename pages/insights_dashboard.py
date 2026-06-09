import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧠 AI Business Insights Dashboard")

df = pd.read_csv("data/customers.csv")

st.subheader("Top Cities by Revenue Potential")

city_income = (
    df.groupby("city")["income"]
    .mean()
    .reset_index()
)

fig = px.bar(
    city_income,
    x="city",
    y="income",
    text_auto=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.subheader("Most Popular Products")

product_count = (
    df["favorite_product"]
    .value_counts()
    .reset_index()
)

product_count.columns = [
    "Product",
    "Count"
]

fig2 = px.bar(
    product_count,
    x="Product",
    y="Count",
    text="Count"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

st.subheader("AI Generated Insights")

avg_income = int(df["income"].mean())

top_city = (
    df.groupby("city")["income"]
    .mean()
    .idxmax()
)

top_product = (
    df["favorite_product"]
    .value_counts()
    .idxmax()
)

churn_rate = round(
    df["churn"].mean()*100,
    2
)

st.success(
    f"Average customer income is ₹{avg_income:,}"
)

st.info(
    f"{top_city} has the highest average income."
)

st.warning(
    f"Most preferred product: {top_product}"
)

st.error(
    f"Current churn rate: {churn_rate}%"
)

st.markdown("### Business Recommendations")

st.write(
    "• Focus marketing campaigns on high-income cities."
)

st.write(
    "• Promote the most popular products through cross-selling."
)

st.write(
    "• Retain low-tenure customers with loyalty programs."
)

st.write(
    "• Target customers with low spending scores."
)