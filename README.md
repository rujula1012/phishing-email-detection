@'
# PhishGuard — Phishing Email Detection

An AIES project that uses Natural Language Processing (NLP) and machine learning to classify email text as **phishing** or **legitimate**.

## Overview

PhishGuard uses TF-IDF to convert email text into numerical features and a trained Logistic Regression model to predict the email category. A Streamlit web application allows users to enter email text and view the prediction.

## Features

- Classifies email text as phishing or legitimate.
- Converts email text into numerical features using TF-IDF.
- Uses a trained Logistic Regression model.
- Displays evaluation metrics and a confusion matrix.
- Provides an interactive Streamlit interface.
- Supports sample-email testing.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Streamlit
- Joblib
- Matplotlib

## Project Structure

```text id="r7p0d4"
phishing-email-detection/
├── app/
│   └── streamlit_app.py
├── evaluation/
│   ├── evaluate_model.py
│   ├── test_emails.py
│   ├── metrics_summary.csv
│   └── confusion_matrix.png
├── model/
│   ├── phishing_model.pkl
│   └── tfidf_vectorizer.pkl
├── dataset/
│   └── cleaned_dataset.csv  (obtained separately)
├── requirements.txt
├── train_model.py
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash id="qz5j9w"
git clone https://github.com/rujula1012/phishing-email-detection.git
cd phishing-email-detection
```

### 2. Create a virtual environment

For Windows PowerShell:

```powershell id="b3s8kt"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell id="t5m2pv"
python -m pip install -r requirements.txt
```

### 4. Prepare the required files

The application requires these saved files:

- `model/phishing_model.pkl`
- `model/tfidf_vectorizer.pkl`

The cleaned dataset is approximately 261 MB and is not included in this repository. Obtain `cleaned_dataset.csv` from the project team and place it in the `dataset/` directory if you need to retrain the model or reproduce the evaluation.

### 5. Run the application

From the project root, run:

```powershell id="w6k1cy"
python -m streamlit run app/streamlit_app.py
```

Streamlit will provide a local URL to open the application in your browser.

## Model Evaluation

The model was evaluated on a held-out test set containing 34,365 emails.

| Metric | Score |
|---|---:|
| Accuracy | 96.62% |
| Weighted Precision | 96.63% |
| Weighted Recall | 96.62% |
| Weighted F1-score | 96.62% |

Evaluation outputs are available in the `evaluation/` directory.

To reproduce the evaluation:

```powershell id="p5j3dz"
python evaluation/evaluate_model.py
```

To test sample emails:

```powershell id="n4v8sy"
python evaluation/test_emails.py
```

## Limitations

- Predictions depend on patterns learned from the training dataset.
- High evaluation scores do not guarantee accurate predictions on every real-world email.
- A prediction of legitimate does not guarantee that an email is safe.
- This is an educational prototype and should not be used as the sole basis for security decisions.

## Project Purpose

This project demonstrates text preprocessing, TF-IDF feature extraction, supervised machine learning, model evaluation, and deployment through a Streamlit interface.
'@ | Set-Content -Encoding utf8 README.md
