
# import streamlit as st
# import joblib

# # Configure the web page
# st.set_page_config(
#     page_title="Phishing Email Detector",
#     page_icon="🛡️",
#     layout="centered"
# )

# # Load the trained model and vectorizer
# model = joblib.load("model/phishing_model.pkl")
# vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# # Page heading
# st.title("🛡️ Phishing Email Detector")
# st.write(
#     "Enter an email below to check whether the trained "
#     "machine learning model classifies it as phishing or legitimate."
# )

# # Email input
# email_text = st.text_area(
#     "Email content",
#     placeholder="Paste the email text here...",
#     height=200
# )

# # Prediction button
# if st.button("Check Email", type="primary"):
#     if not email_text.strip():
#         st.warning("Please enter some email text first.")
#     else:
#         email_features = vectorizer.transform([email_text])
#         prediction = model.predict(email_features)[0]

#         if prediction == "phishing":
#             st.error("⚠️ Prediction: PHISHING")
#             st.write(
#                 "The model classifies this email as phishing. "
#                 "Be cautious and verify the sender and links."
#             )
#         else:
#             st.success("✅ Prediction: LEGITIMATE")
#             st.write(
#                 "The model classifies this email as legitimate. "
#                 "This prediction does not guarantee that the email is safe."
#             )

# st.caption(
#     "This tool provides a machine-learning prediction, "
#     "not a guarantee of email safety."
# )


import streamlit as st
import joblib
from pathlib import Path

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="PhishGuard | Email Security",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- CUSTOM STYLING ----------------
st.markdown("""
<style>
.main .block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    padding: 1.8rem;
    border-radius: 16px;
    background: linear-gradient(120deg, #10243a, #205072);
    color: white;
    margin-bottom: 1.5rem;
}
.hero h1 {
    color: white;
    margin-bottom: 0.5rem;
}
.hero p {
    color: #e2edf5;
    font-size: 1.05rem;
}
.result {
    padding: 1.4rem;
    border-radius: 14px;
    border: 1px solid #d1d5db;
    margin-top: 1rem;
}
.small-note {
    color: #6b7280;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD TRAINED MODEL ----------------
ROOT = Path(__file__).resolve().parent.parent

@st.cache_resource
def load_artifacts():
    model = joblib.load(ROOT / "model" / "phishing_model.pkl")
    vectorizer = joblib.load(ROOT / "model" / "tfidf_vectorizer.pkl")
    return model, vectorizer

try:
    model, vectorizer = load_artifacts()
except Exception as error:
    st.error("Could not load the trained model files.")
    st.caption("Check that both files exist inside the project's model folder.")
    st.stop()

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <h1>🛡️ PhishGuard</h1>
    <p>AI-powered phishing email detection</p>
    <p>Analyze email text with a machine-learning model
    trained to classify messages as phishing or legitimate.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("About the Project")
    st.write(
        "PhishGuard uses TF-IDF to convert email text into "
        "numerical features and a trained Logistic Regression "
        "model to predict its category."
    )
    st.divider()
    st.subheader("How to use")
    st.write("1. Paste the email text.")
    st.write("2. Click Analyze Email.")
    st.write("3. Review the model's prediction.")
    st.divider()
    st.caption("A student machine-learning project.")

# ---------------- EMAIL INPUT ----------------
st.subheader("Analyze an email")
st.write("Paste the email's subject and/or body below.")

if "email_input" not in st.session_state:
    st.session_state.email_input = ""

def clear_email():
    st.session_state.email_input = ""

with st.form("email_analysis_form"):
    email_text = st.text_area(
        "Email content",
        key="email_input",
        height=220,
        placeholder=(
            "Example: Your account requires verification. "
            "Click the link below..."
        )
    )
    analyze = st.form_submit_button(
        "🔎 Analyze Email",
        type="primary",
        use_container_width=True
    )

st.button(
    "Clear email",
    on_click=clear_email
)

# ---------------- PREDICTION ----------------
if analyze:
    if not email_text.strip():
        st.warning("Please enter some email text first.")
    else:
        features = vectorizer.transform([email_text])
        prediction = model.predict(features)[0]

        st.divider()
        st.subheader("Analysis Result")

        if prediction == "phishing":
            st.error("🚨 Predicted as PHISHING")
            st.write(
                "The model identified this email as phishing. "
                "Avoid clicking links or sharing sensitive information "
                "until you independently verify the sender."
            )
        else:
            st.success("✅ Predicted as LEGITIMATE")
            st.write(
                "The model classified this email as legitimate. "
                "This does not guarantee that the message is safe."
            )

        # Show model probability when supported
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(features)[0]
            classes = list(model.classes_)
            predicted_index = classes.index(prediction)
            score = float(probabilities[predicted_index])

            st.metric(
                "Model confidence score",
                f"{score:.1%}"
            )
            st.caption(
                "This is the model's estimated probability for its "
                "predicted class, not a guarantee of correctness."
            )

# ---------------- DISCLAIMER ----------------
st.divider()
st.markdown(
    '<p class="small-note">Educational prototype only. '
    'Do not rely on this tool as the sole basis for security decisions. '
    'Avoid entering real passwords, confidential data, or sensitive emails.</p>',
    unsafe_allow_html=True
)
