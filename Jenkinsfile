pipeline {
    agent any

    environment {
        KUBECONFIG_CREDENTIALS_ID = 'kubeconfig' // substitua pelo ID da credencial do arquivo kubeconfig
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/kaiopiterson/globo'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t comments-api .'
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh '''
                        docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD
                        docker tag comments-api $DOCKERHUB_USERNAME/comments-api:latest
                        docker push $DOCKERHUB_USERNAME/comments-api:latest
                    '''
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: env.KUBECONFIG_CREDENTIALS_ID, variable: 'KUBECONFIG')]) {
                    sh 'kubectl apply -f deployment.yaml --kubeconfig=$KUBECONFIG'
                    sh 'kubectl apply -f service_nodePort.yaml --kubeconfig=$KUBECONFIG'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

