import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv(
    "data/customers.csv"
)

X = data[
    [
        'income',
        'spending_score',
        'tenure'
    ]
]

y = data['churn']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

joblib.dump(
    model,
    "models/churn_model.pkl"
)

print("Model Trained Successfully")