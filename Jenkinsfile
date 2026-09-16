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

        stage('Credentials Demo') {
            steps {
                withCredentials([
                    string(
                        credentialsId: 'demo-secret',
                        variable: 'MY_SECRET'
                    )
                ]) {
                    sh 'echo "Secret is available to the pipeline"'
                    sh 'echo "Secret length: ${#MY_SECRET}"'
                }
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
