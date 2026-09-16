pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'docker-registry-002.zeuslearning.com/zeuslearning/python:3.12-slim'
                    reuseNode true
                }
            }

            steps {
                sh '''
                    pip install -r requirements.txt
                    pytest --junitxml=test-results.xml
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
        }
    }
}
