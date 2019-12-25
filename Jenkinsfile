pipeline {
    agent { dockerfile true }
    stages {
        stage('Test phase') {
            steps {
                sh 'node --version'
                sh 'svn --version'
            }
        }
    }
}
