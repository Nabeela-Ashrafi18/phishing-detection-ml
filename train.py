import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

from feature_extraction import extract_features

# Load dataset
df = pd.read_csv("malicious_phish.csv")

# Convert labels
df["label"] = df["type"].apply(
    lambda x: 0 if x == "benign" else 1
)

# Generate features from URLs
X = df["url"].apply(extract_features)

# Convert list of features into dataframe
X = pd.DataFrame(X.tolist())

# Target
y = df["label"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

# Save model
joblib.dump(model, "phishing_model.pkl")

print("Model saved successfully!")
