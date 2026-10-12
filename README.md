<<<<<<< HEAD
=======

@'
>>>>>>> 24c1404 (Improve project documentation)
# PhishGuard — Phishing Email Detection

An AIES project that uses Natural Language Processing (NLP) and machine learning to classify email text as **phishing** or **legitimate**.

## Overview

PhishGuard uses TF-IDF to convert email text into numerical features and a trained Logistic Regression model to predict the email category. A Streamlit web interface allows users to enter email text and view the prediction.

## Features

- Classifies email text as phishing or legitimate.
- Uses TF-IDF text vectorization.
- Uses a trained Logistic Regression classifier.
- Displays evaluation metrics and a confusion matrix.
- Provides an interactive Streamlit interface.
- Supports testing sample emails.

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

```text
phishing-email-detection/
├── app/
│   └── streamlit_app.py
├── dataset/
│   └── cleaned_dataset.csv
├── evaluation/
│   ├── evaluate_model.py
│   ├── test_emails.py
│   ├── metrics_summary.csv
│   └── confusion_matrix.png
├── model/
│   ├── phishing_model.pkl
│   └── tfidf_vectorizer.pkl
├── .gitignore
├── requirements.txt
├── README.md
└── train_model.py
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/rujula1012/phishing-email-detection.git
cd phishing-email-detection
```

<<<<<<< HEAD
### 2. Create and activate a virtual environment

Windows PowerShell:
=======
### 2. Create a virtual environment
>>>>>>> 24c1404 (Improve project documentation)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

<<<<<<< HEAD
### 4. Prepare the dataset and model files

The application requires these files:

- `dataset/cleaned_dataset.csv`
- `model/phishing_model.pkl`
- `model/tfidf_vectorizer.pkl`

The cleaned dataset is not included in the Git repository because of its file size. Obtain it from the project team and place it in the `dataset/` directory.

The saved model and vectorizer are included in the repository. If they are unavailable, regenerate them by running the training script after placing the dataset in the correct location.

### 5. Run the web application

From the project root, run:
=======
### 4. Prepare the required files

The application requires:

- `model/phishing_model.pkl`
- `model/tfidf_vectorizer.pkl`

To retrain the model or reproduce evaluation, obtain the cleaned dataset from the project team and place it at `dataset/cleaned_dataset.csv`. The dataset is not included in this repository because of its size.

### 5. Run the application

From the project root:
>>>>>>> 24c1404 (Improve project documentation)

```bash
python -m streamlit run app/streamlit_app.py
```

<<<<<<< HEAD
Streamlit will provide a local URL where you can open the application.

## Model Evaluation

The saved model was evaluated on a held-out test set using accuracy, precision, recall, F1-score, a classification report, and a confusion matrix.
=======
## Model Evaluation

The model was evaluated on a held-out test set containing 34,365 emails.
>>>>>>> 24c1404 (Improve project documentation)

| Metric | Score |
|---|---:|
| Accuracy | 96.62% |
| Weighted Precision | 96.63% |
| Weighted Recall | 96.62% |
| Weighted F1-score | 96.62% |

<<<<<<< HEAD
The test set contained 34,365 emails.

Evaluation outputs are available in the `evaluation/` directory.
=======
Evaluation outputs are saved in the `evaluation/` directory.
>>>>>>> 24c1404 (Improve project documentation)

To reproduce the evaluation, run:

```bash
python evaluation/evaluate_model.py
```

<<<<<<< HEAD
To test the sample emails, run:
=======
To test sample emails, run:
>>>>>>> 24c1404 (Improve project documentation)

```bash
python evaluation/test_emails.py
```

## Limitations

<<<<<<< HEAD
- Predictions depend on the training dataset and the patterns learned by the model.
- High evaluation scores do not guarantee accurate predictions for every real-world email.
- A prediction of legitimate does not guarantee that an email is safe.
=======
- Predictions depend on the patterns learned from the training dataset.
- High evaluation scores do not guarantee accurate predictions on every real-world email.
- A legitimate prediction does not guarantee that an email is safe.
>>>>>>> 24c1404 (Improve project documentation)
- This project is an educational prototype and should not be used as the sole basis for security decisions.

## Project Purpose

<<<<<<< HEAD
This project demonstrates text preprocessing, feature extraction using TF-IDF, supervised machine learning, model evaluation, and deployment through a Streamlit interface.
=======
This project demonstrates text preprocessing, TF-IDF feature extraction, supervised machine learning, model evaluation, and deployment through a Streamlit interface.
'@ | Set-Content -Encoding utf8 README.md
>>>>>>> 24c1404 (Improve project documentation)
