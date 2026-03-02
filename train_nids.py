import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

print("Loading cleaned dataset...")

data = pd.read_csv("dataset/cleaned_cicids.csv")
data.columns = data.columns.str.strip()

label_column = data.columns[-1]

X = data.drop(label_column, axis=1)
# Save first 5 rows as test file
X.head(5).to_csv("test_input.csv", index=False)
print("Test file created successfully!")
y = data[label_column]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 🔥 Evaluate model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

joblib.dump(model, "models/nids_model.pkl")

print("\nNIDS Model Trained, Evaluated and Saved Successfully!")