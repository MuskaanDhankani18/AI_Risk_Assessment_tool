import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


data = {
    "financial_stability": np.random.uniform(0, 1, 500),
    "market_risk": np.random.uniform(0, 1, 500),
    "operational_risk": np.random.uniform(0, 1, 500),
    "compliance_risk": np.random.uniform(0, 1, 500),
    "cybersecurity_risk": np.random.uniform(0, 1, 500),
    "supply_chain_risk": np.random.uniform(0, 1, 500),
    "reputation_risk": np.random.uniform(0, 1, 500),
}

df = pd.DataFrame(data)
df["risk_score"] = (df["market_risk"] + df["operational_risk"] + 
                    df["compliance_risk"] + df["cybersecurity_risk"] + 
                    df["supply_chain_risk"] + df["reputation_risk"]) / 6


x = df.drop("risk_score", axis=1)
y = df["risk_score"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(x_train, y_train)


y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Model MAE: {mae:.4f}")


joblib.dump(model, "risk_model.pkl")
print("Model trained and saved successfully!")
