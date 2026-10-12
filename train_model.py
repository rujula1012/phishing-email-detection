
import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

data = pd.read_csv("dataset/cleaned_dataset.csv")

data = data.dropna(subset=["body", "label"])
data = data.drop_duplicates(subset=["body"])

X = data["body"].astype(str)
y = data["label"].astype(str).str.strip().str.lower()

print("Dataset size:", data.shape)
print("Labels:", y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

vectorizer = TfidfVectorizer(max_features=10000, stop_words="english")
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

predictions = model.predict(X_test_tfidf)

print("\nAccuracy:", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions, average="weighted", zero_division=0))
print("Recall:", recall_score(y_test, predictions, average="weighted", zero_division=0))
print("F1-score:", f1_score(y_test, predictions, average="weighted", zero_division=0))

print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/phishing_model.pkl")
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")

print("\nModel and TF-IDF vectorizer saved successfully!")
