# 🤖 AI Customer Intelligence Platform

## 📊 Overview

The **AI Customer Intelligence Platform** is a complete end-to-end **machine learning + data analytics web application** built using **Streamlit, Python, and Plotly**.  

It helps businesses analyze customer behavior, perform segmentation, predict churn, and generate AI-powered insights using interactive dashboards.

This project demonstrates real-world data science workflow including:
- Data generation
- Model training
- Prediction system
- Visualization dashboards
- Modular Streamlit pages

---

# 🚀 Features

## 📌 1. Customer Dashboard
- Total customers overview
- Revenue analysis
- Churn rate tracking
- Income & spending insights
- City-wise analysis

---

## ⚠ 2. Churn Prediction System
- Predict whether a customer will churn
- Uses ML model (RandomForestClassifier)
- Inputs:
  - Income
  - Spending Score
  - Tenure
- Outputs:
  - Churn probability
  - Risk classification

---

## 👥 3. Customer Segmentation (K-Means)
- Groups customers into segments based on:
  - Income
  - Spending Score
- Identifies:
  - High-value customers
  - Low-value customers
- Includes cluster visualization

---

## 🎯 4. Recommendation System
- Suggests products based on:
  - Similar customer behavior
  - Category matching
- Personalized customer insights

---

## 📈 5. Insights Dashboard
- Business intelligence summaries
- Trend analysis
- Key performance insights
- Data-driven decision support

---

## 📊 6. Interactive Visualizations
- Plotly charts:
  - Bar charts
  - Pie charts
  - Scatter plots
  - Box plots
- Fully interactive dashboards

---

# 🧠 Machine Learning Models

## 1. Customer Churn Prediction
- Algorithm: Random Forest Classifier
- Features:
  - Income
  - Spending Score
  - Tenure
- Output:
  - 0 → Stay
  - 1 → Churn

---

## 2. Customer Segmentation
- Algorithm: K-Means Clustering
- Features:
  - Income
  - Spending Score
- Clusters:
  - High value
  - Medium value
  - Low value
  - At-risk customers

---

# 🏗 Project Structure

AI_Customer_Intelligence_Platform/
│
├── app.py
│
├── pages/
│   ├── dashboard.py
│   ├── churn.py
│   ├── segmentation.py
│   ├── prediction.py
│   ├── recommendations.py
│   ├── insights_dashboard.py
│
├── data/
│   └── customers.csv
│
├── assets/
│   ├── logo.png
│   ├── styles.css
│
├── models/
│   └── churn_model.pkl
│
├── generate_dataset.py
├── train_models.py
├── requirements.txt
└── README.md

---

# ⚙ Installation & Setup

## 1️⃣ Clone the repository
git clone https://github.com/Akhila1128/PROJECT1-DA.git
cd PROJECT1-DA

## 2️⃣ Install dependencies
pip install -r requirements.txt

If not available:
pip install streamlit pandas plotly scikit-learn numpy

## 3️⃣ Run the application
streamlit run app.py

---

# 📊 Dataset Information

- Customer ID
- Name
- Age
- Gender
- City
- Income
- Spending Score
- Tenure
- Churn status

---

# 🧪 Tech Stack

- Streamlit
- Python
- Scikit-learn
- Plotly
- Pandas
- NumPy

---

# 👨‍💻 Author

Akhila K  
AI & Data Science Project  
Summer Training Project
