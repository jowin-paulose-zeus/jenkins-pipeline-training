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
                sh 'python3 run_tests.py'
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
}p
