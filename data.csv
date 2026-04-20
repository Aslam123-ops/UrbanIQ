import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data.csv")

X = df[["traffic"]]
y = df["energy"]

# Train model
model = LinearRegression()
model.fit(X, y)

def predict_energy(traffic):
    prediction = model.predict([[traffic]])
    return int(prediction[0])
