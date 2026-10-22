pipeline {
    agent any

    triggers { githubPush() }

    environment {
        IMAGE_NAME = 'YOUR_DOCKERHUB_USER/phishing-detector'
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Build & Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt pytest
                    python -m py_compile app/streamlit_app.py train_model.py
                    pytest -q tests
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                 usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    sh '''
                        echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
                        docker push $IMAGE_NAME:$IMAGE_TAG
                        docker push $IMAGE_NAME:latest
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                sh '''
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    kubectl set image deployment/phishing-detector phishing-detector=$IMAGE_NAME:$IMAGE_TAG
                    kubectl rollout status deployment/phishing-detector --timeout=300s
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                    kubectl get pods -o wide
                    kubectl get deployment
                    kubectl get svc
                    curl -s -o /dev/null -w "App HTTP status: %{http_code}\\n" http://$(minikube ip):30085
                '''
            }
        }
    }
}