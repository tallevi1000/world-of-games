pipeline {
    agent any
    stages {
        stage('test') {
            agent {
                docker { image 'python:3' }
            }
            steps {
                sh 'date'
            }
        }
    }
}
