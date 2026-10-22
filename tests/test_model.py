import joblib

def test_model_loads_and_predicts():
    model = joblib.load("model/phishing_model.pkl")
    vec = joblib.load("model/tfidf_vectorizer.pkl")
    X = vec.transform(["Your account is suspended. Click here to verify your password now"])
    assert len(model.predict(X)) == 1