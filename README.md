# PhishGuard: Phishing Email Detection Using Machine Learning

## 1. Project Overview

PhishGuard is a machine-learning-based web application that detects potentially phishing emails by analyzing their text. It uses TF-IDF for text feature extraction and a Logistic Regression classifier to predict whether an email is phishing or legitimate.

The project also demonstrates an automated CI/CD pipeline using GitHub, Jenkins, Docker, Docker Hub, and Kubernetes.

## 2. Objectives

- Detect phishing emails using machine learning.
- Convert email text into numerical features using TF-IDF.
- Classify emails using Logistic Regression.
- Provide an interactive web interface using Streamlit.
- Automate testing, Docker image creation, image publishing, and deployment.
- Deploy the application using Kubernetes with two replicas.

## 3. Technology Stack

- **Programming language:** Python
- **Machine learning:** Scikit-learn, TF-IDF, Logistic Regression
- **Web framework:** Streamlit
- **Data processing:** Pandas, NumPy
- **Version control:** Git and GitHub
- **CI/CD:** Jenkins
- **Containerization:** Docker
- **Container registry:** Docker Hub
- **Orchestration:** Kubernetes using Minikube
- **Cloud platform:** AWS EC2
- **Testing:** Pytest

## 4. System Architecture

The project follows this automated workflow:

1. A developer pushes code changes to GitHub.
2. A GitHub webhook triggers the Jenkins pipeline.
3. Jenkins checks out the latest source code.
4. Dependencies are installed and tests are executed.
5. A Docker image is built.
6. The image is pushed to Docker Hub.
7. Jenkins deploys the updated image to Kubernetes.
8. Kubernetes manages two application replicas.
9. The application is accessed through the configured service and port-forward.

**Pipeline flow:**

GitHub → Jenkins → Build and Test → Docker Build → Docker Hub → Kubernetes → Streamlit Application

## 5. Machine Learning Implementation

### TF-IDF

Term Frequency–Inverse Document Frequency (TF-IDF) converts email text into numerical features. It represents words according to their importance within a document relative to the dataset.

### Logistic Regression

Logistic Regression is the classification algorithm used to predict whether an email is phishing or legitimate based on the extracted text features.

### Prediction workflow

1. The user enters email content.
2. The application preprocesses and vectorizes the text.
3. The trained Logistic Regression model generates a prediction.
4. The interface displays the predicted category and associated confidence information.

## 6. Dataset and Model

The project uses a labeled email dataset containing legitimate and phishing examples.

- **Dataset size:** 171,822 records
- **Legitimate emails:** 89,261
- **Phishing emails:** 82,561
- **Trained model:** `model/phishing_model.pkl`
- **TF-IDF vectorizer:** `model/tfidf_vectorizer.pkl`

The trained model and vectorizer are loaded by the Streamlit application for predictions.

## 7. Model Evaluation

The recorded evaluation results are:

| Metric | Score |
|---|---:|
| Accuracy | 96.62% |
| Precision | 96.63% |
| Recall | 96.62% |
| F1-score | 96.62% |

The model was evaluated using a held-out test set. These results reflect performance on that evaluation split and do not guarantee equivalent performance on all real-world emails.

## 8. CI/CD Pipeline

The Jenkins pipeline is defined in the `Jenkinsfile`.

### Pipeline stages

1. **Checkout:** Retrieves source code from GitHub.
2. **Build & Test:** Installs dependencies, compiles Python files, and runs the test suite.
3. **Docker Build:** Builds the container image and tags it using the build number and `latest`.
4. **Push Image:** Publishes the image to Docker Hub using Jenkins credentials.
5. **Deploy to Minikube:** Applies Kubernetes configuration, updates the image, and waits for rollout completion.
6. **Verify:** Checks deployment resources and application accessibility.

The pipeline is configured to respond to GitHub push events through a webhook.

## 9. Docker and Kubernetes Deployment

Docker packages the application and its dependencies into a portable image.

The Kubernetes deployment configuration defines two replicas of the application. A NodePort service exposes container port `8501` through NodePort `30085`.

The deployment files are stored in the `k8s/` directory.

The application was deployed to a Minikube cluster running on an AWS EC2 instance.

## 10. Project Structure

```text
phishing-email-detection/
├── app/
│   └── streamlit_app.py
├── dataset/
│   └── cleaned_dataset.csv
├── evaluation/
│   ├── confusion_matrix.png
│   └── metrics_summary.csv
├── model/
│   ├── phishing_model.pkl
│   └── tfidf_vectorizer.pkl
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── tests/
├── screenshots/
├── train_model.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── Jenkinsfile
└── README.md
```

## 11. Running the Application Locally

### Prerequisites

- Python installed
- Git installed
- Project dependencies available

### Setup

Clone the repository:

```bash
git clone https://github.com/rujula1012/phishing-email-detection.git
cd phishing-email-detection
```

Create and activate a virtual environment on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app/streamlit_app.py
```

Open the local URL displayed in the terminal.

## 12. Screenshots and Evidence

The `screenshots/` directory contains evidence of the implementation and deployment, including:

- Kubernetes node and pod status
- Jenkins job and pipeline configuration
- Successful Jenkins pipeline execution
- Docker Hub image tags
- Kubernetes deployment and service status
- Live PhishGuard v2 application
- GitHub commit and webhook evidence

## 13. Results

The project demonstrates a complete machine-learning application workflow, from email text classification to containerized deployment. The application was successfully built and deployed through Jenkins, with the updated PhishGuard v2 interface verified in the browser.

The pipeline integrates source control, automated testing, container image publishing, and Kubernetes deployment.

## 14. Limitations and Future Scope

- Improve detection of previously unseen phishing techniques.
- Evaluate the model on additional real-world email datasets.
- Add stronger preprocessing and feature engineering.
- Introduce authentication and access control where required.
- Configure persistent service exposure instead of relying on a manually started port-forward.
- Add monitoring, logging, and model retraining workflows.

## 15. Repository

GitHub: https://github.com/rujula1012/phishing-email-detection

Docker Hub: https://hub.docker.com/r/rsk1012/phishing-detector

## 16. Conclusion

PhishGuard combines machine learning with DevOps practices to create and deploy a phishing email detection application. The project demonstrates TF-IDF-based feature extraction, Logistic Regression classification, a Streamlit interface, and an automated CI/CD pipeline using GitHub, Jenkins, Docker, and Kubernetes.
