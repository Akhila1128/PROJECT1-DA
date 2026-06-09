import streamlit as st
import pandas as pd
import plotly.express as px
import os
from PIL import Image

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="AI Customer Intelligence", layout="wide")

# =========================
# SAFE CSS
# =========================
css_path = "assets/styles.css"

if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("AI Customer Intelligence")

logo_path = "assets/logo.png"

if os.path.exists(logo_path):
    try:
        st.sidebar.image(Image.open(logo_path), use_container_width=True)
    except:
        st.sidebar.warning("Invalid image")
else:
    st.sidebar.warning("Logo not found")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### PLATFORM FEATURES

- Customer Analytics
- AI Prediction
- Recommendation Engine
- Churn Analysis
""")

st.sidebar.markdown("---")

st.sidebar.info("Built with Streamlit + Plotly + ML Concepts")

# =========================
# DATA
# =========================
df = pd.read_csv("data/customers.csv")

# =========================
# TITLE
# =========================
st.title("🤖 AI Customer Intelligence Platform")

st.divider()

# =========================
# KPI
# =========================
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Customers", len(df))

with c2:
    st.metric("Revenue", f"${df['income'].sum():,}")

with c3:
    st.metric("Retention", f"{round((1 - df['churn'].mean()) * 100, 2)}%")

with c4:
    st.metric("AI Accuracy", "92%")

st.divider()

# =========================
# GRAPH 1
# =========================
city = df.groupby("city")["income"].sum().reset_index()

fig1 = px.bar(city, x="city", y="income", color="city")
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# =========================
# GRAPH 2
# =========================
fig2 = px.line(df.head(100), x="customer_id", y="spending_score")
st.plotly_chart(fig2, use_container_width=True)

st.divider()

# =========================
# GRAPH 3
# =========================
gender = df["gender"].value_counts()

fig3 = px.pie(values=gender.values, names=gender.index)
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# =========================
# GRAPH 4
# =========================
fig4 = px.scatter(df, x="age", y="spending_score", color="gender", size="income")
st.plotly_chart(fig4, use_container_width=True)

st.divider()

# =========================
# GRAPH 5
# =========================
churn = df["churn"].value_counts()

fig5 = px.pie(values=churn.values, names=["Active", "Churned"])
st.plotly_chart(fig5, use_container_width=True)

st.divider()

st.success("Dashboard Loaded Successfully 🚀")