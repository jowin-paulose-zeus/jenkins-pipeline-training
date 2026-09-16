pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                    .venv/bin/pytest --junitxml=test-results.xml
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
