
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# Load the dataset
data = pd.read_csv("dataset/cleaned_dataset.csv")
data = data.dropna(subset=["body", "label"])
data = data.drop_duplicates(subset=["body"])

X = data["body"].astype(str)
y = data["label"].astype(str).str.strip().str.lower()

# Use the same test split as the training script
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Load the saved model and TF-IDF vectorizer
model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# Convert test emails into numerical features
X_test_tfidf = vectorizer.transform(X_test)

# Predict email categories
predictions = model.predict(X_test_tfidf)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(
    y_test, predictions, average="weighted", zero_division=0
)
recall = recall_score(
    y_test, predictions, average="weighted", zero_division=0
)
f1 = f1_score(
    y_test, predictions, average="weighted", zero_division=0
)

print("MODEL EVALUATION RESULTS")
print("------------------------")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# Save metrics to a CSV file
os.makedirs("evaluation", exist_ok=True)

metrics = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1-score"],
    "Score": [accuracy, precision, recall, f1]
})

metrics.to_csv("evaluation/metrics_summary.csv", index=False)

# Save confusion matrix as an image
labels = ["legitimate", "phishing"]
cm = confusion_matrix(y_test, predictions, labels=labels)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=labels
)
display.plot(values_format="d")
plt.title("Phishing Email Detection - Confusion Matrix")
plt.tight_layout()
plt.savefig("evaluation/confusion_matrix.png", dpi=200)
plt.close()

print("\nSaved evaluation/metrics_summary.csv")
print("Saved evaluation/confusion_matrix.png")
