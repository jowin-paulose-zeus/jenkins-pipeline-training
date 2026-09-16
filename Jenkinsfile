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
                    python3 -m pip install -r requirements.txt
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
