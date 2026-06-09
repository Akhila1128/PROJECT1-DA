from faker import Faker
import pandas as pd
import random

fake = Faker()

rows = []

cities = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Chennai",
    "Pune"
]

products = [
    "iPhone",
    "Laptop",
    "Shoes",
    "Watch",
    "Gaming Console",
    "Headphones",
    "Smart TV",
    "Fitness Band",
    "Camera",
    "Tablet"
]

categories = [
    "Electronics",
    "Fashion",
    "Gaming",
    "Fitness",
    "Accessories"
]

for i in range(1, 501):

    income = random.randint(20000, 150000)

    spending = random.randint(1, 100)

    tenure = random.randint(1, 60)

    visits = random.randint(1, 30)

    if tenure < 12 and spending < 40:
        churn = 1
    else:
        churn = 0

    rows.append([
        i,
        fake.name(),
        random.randint(18,60),
        random.choice(["Male","Female"]),
        random.choice(cities),
        income,
        spending,
        tenure,
        visits,
        random.choice(products),
        random.choice(categories),
        random.randint(1,20),
        churn
    ])

df = pd.DataFrame(rows, columns=[
    "customer_id",
    "name",
    "age",
    "gender",
    "city",
    "income",
    "spending_score",
    "tenure",
    "monthly_visits",
    "favorite_product",
    "favorite_category",
    "purchase_frequency",
    "churn"
])

df.to_csv(
    "data/customers.csv",
    index=False
)

print("500 Customer Records Generated")