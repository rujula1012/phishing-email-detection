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


## CI/CD Implementation

### Project Workflow

The Phishing Email Detection application uses a CI/CD workflow to automate testing, containerization, and deployment.

1. **Source Control:** GitHub stores the application source code and pipeline configuration.
2. **Continuous Integration:** Jenkins checks out the repository and runs Python syntax checks and model prediction tests.
3. **Containerization:** Docker builds a container image containing the Streamlit application and trained model.
4. **Image Registry:** The container image is pushed to Docker Hub.
5. **Continuous Deployment:** Kubernetes manifests define the application Deployment and Service, with Minikube used as the local Kubernetes environment.
6. **Verification:** Deployment status, running pods, and application accessibility are checked.

### CI/CD Files

- `Dockerfile` — defines the application container image.
- `.dockerignore` — excludes unnecessary files from the Docker build context.
- `Jenkinsfile` — defines the automated pipeline stages.
- `tests/test_model.py` — checks model loading and prediction.
- `k8s/deployment.yaml` — defines the Kubernetes Deployment.
- `k8s/service.yaml` — defines how the application is exposed.

### Testing

The model prediction test is executed using:

```bash
python -m pytest -q tests
```

The test verifies that the saved model and TF-IDF vectorizer load successfully and that the model returns a prediction for a sample email.

### Deployment Environment

The intended deployment environment consists of Jenkins running on AWS EC2, Docker Hub for image storage, and Minikube for Kubernetes deployment.

The pipeline must be executed successfully to verify the complete CI/CD workflow.
