import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Dashboard", layout="wide")

st.title("📊 AI Customer Analytics Dashboard")

# ==========================
# LOAD DATA
# ==========================
df = pd.read_csv("data/customers.csv")

# ==========================
# SIDEBAR FILTERS
# ==========================
st.sidebar.header("🔍 Filters")

city_filter = st.sidebar.multiselect(
    "Select City",
    df["city"].unique(),
    default=df["city"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    df["gender"].unique(),
    default=df["gender"].unique()
)

filtered_df = df[
    (df["city"].isin(city_filter)) &
    (df["gender"].isin(gender_filter))
]

# ==========================
# KPI SECTION
# ==========================
st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", len(filtered_df))
col2.metric("Avg Income", f"₹{int(filtered_df['income'].mean()):,}")
col3.metric("Avg Spending", round(filtered_df["spending_score"].mean(), 1))
col4.metric("Churn Rate", f"{round(filtered_df['churn'].mean()*100,1)}%")

st.divider()

# ==========================
# CITY ANALYSIS
# ==========================
st.subheader("🏙 Customers by City")

city_data = filtered_df["city"].value_counts().reset_index()
city_data.columns = ["City", "Customers"]

fig1 = px.bar(city_data, x="City", y="Customers", text="Customers", color="City")
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# ==========================
# INCOME DISTRIBUTION
# ==========================
st.subheader("💰 Income Distribution")

fig2 = px.histogram(filtered_df, x="income", nbins=20)
st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ==========================
# GENDER DISTRIBUTION
# ==========================
st.subheader("👥 Gender Distribution")

gender_data = filtered_df["gender"].value_counts()

fig3 = px.pie(values=gender_data.values, names=gender_data.index)
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ==========================
# SCATTER PLOT
# ==========================
st.subheader("📈 Income vs Spending Score")

fig4 = px.scatter(
    filtered_df,
    x="income",
    y="spending_score",
    color="gender",
    size="age",
    hover_data=["city"]
)

st.plotly_chart(fig4, use_container_width=True)

st.divider()

# ==========================
# CHURN ANALYSIS
# ==========================
st.subheader("⚠ Churn Analysis")

fig5 = px.pie(
    values=filtered_df["churn"].value_counts().values,
    names=["Stay", "Churn"]
)

st.plotly_chart(fig5, use_container_width=True)

st.divider()

# ==========================
# HIGH RISK CUSTOMERS
# ==========================
st.subheader("🚨 High Risk Customers")

risk_customers = filtered_df[
    (filtered_df["spending_score"] < 40) &
    (filtered_df["income"] < filtered_df["income"].mean())
]

st.dataframe(
    risk_customers[[
        "customer_id",
        "name",
        "city",
        "income",
        "spending_score",
        "churn"
    ]],
    use_container_width=True
)

st.divider()

# ==========================
# SUMMARY INSIGHT
# ==========================
st.subheader("🤖 AI Insights")

st.info("High income + high spending customers drive maximum revenue.")
st.warning("Low spending customers have higher churn risk.")
st.success("Urban cities show higher customer engagement.")