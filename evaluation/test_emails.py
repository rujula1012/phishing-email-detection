
import joblib

# Load the saved model and vectorizer
model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# Sample emails for testing
emails = [
    "Congratulations! You won a prize. Click here to claim it now.",
    "Hi team, the meeting is scheduled for tomorrow at 10 AM.",
    "Your bank account will be blocked. Verify your password immediately."
]

# Convert email text into numerical features
email_features = vectorizer.transform(emails)

# Predict the category of each email
predictions = model.predict(email_features)

# Display the results
for email, prediction in zip(emails, predictions):
    print("\nEmail:", email)
    print("Predicted category:", prediction)
