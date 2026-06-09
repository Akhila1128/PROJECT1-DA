import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

st.set_page_config(page_title="Customer Segmentation", layout="wide")

st.title("👥 AI Customer Segmentation (KMeans)")

# ==========================
# LOAD DATA
# ==========================
df = pd.read_csv("data/customers.csv")

# ==========================
# FEATURES
# ==========================
X = df[["income", "spending_score"]]

# ==========================
# ELBOW METHOD (Optional Insight)
# ==========================
st.subheader("📊 Optimal Cluster Selection (Elbow Method)")

inertia = []
K_range = range(1, 10)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertia.append(km.inertia_)

elbow_df = pd.DataFrame({
    "K": list(K_range),
    "Inertia": inertia
})

fig_elbow = px.line(elbow_df, x="K", y="Inertia", markers=True)
st.plotly_chart(fig_elbow, use_container_width=True)

st.divider()

# ==========================
# MODEL TRAINING
# ==========================
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df["Segment"] = kmeans.fit_predict(X)

# ==========================
# FILTER
# ==========================
st.sidebar.header("🔍 Filter Segments")

selected_segments = st.sidebar.multiselect(
    "Select Segment",
    sorted(df["Segment"].unique()),
    default=sorted(df["Segment"].unique())
)

filtered_df = df[df["Segment"].isin(selected_segments)]

# ==========================
# SCATTER PLOT
# ==========================
st.subheader("📍 Customer Segments Visualization")

fig = px.scatter(
    filtered_df,
    x="income",
    y="spending_score",
    color=filtered_df["Segment"].astype(str),
    hover_data=["customer_id", "name", "age", "city"],
    title="Customer Clusters"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# CLUSTER COUNTS
# ==========================
st.subheader("📊 Segment Distribution")

cluster_counts = df["Segment"].value_counts().reset_index()
cluster_counts.columns = ["Segment", "Customers"]

fig2 = px.bar(
    cluster_counts,
    x="Segment",
    y="Customers",
    text="Customers",
    color="Segment"
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ==========================
# SEGMENT SUMMARY
# ==========================
st.subheader("📌 Segment Profiling")

summary = df.groupby("Segment")[["income", "spending_score"]].mean()

st.dataframe(summary)

st.divider()

# ==========================
# HIGH VALUE / LOW VALUE SEGMENTS
# ==========================
st.subheader("💰 Segment Insights")

high_value = summary["income"].idxmax()
low_value = summary["income"].idxmin()

st.success(f"🏆 High Value Segment: {high_value}")
st.warning(f"⚠ Low Value Segment: {low_value}")

st.divider()

# ==========================
# OPTIONAL 3D VISUALIZATION
# ==========================
st.subheader("📈 3D Cluster View")

fig3d = px.scatter_3d(
    df,
    x="income",
    y="spending_score",
    z="age",
    color=df["Segment"].astype(str),
    hover_data=["name", "city"]
)

st.plotly_chart(fig3d, use_container_width=True)

st.divider()

# ==========================
# CUSTOMER TABLE
# ==========================
st.subheader("👥 Customers in Selected Segments")

st.dataframe(
    filtered_df[[
        "customer_id",
        "name",
        "city",
        "income",
        "spending_score",
        "Segment"
    ]],
    use_container_width=True
)