pipeline {
    agent any
    stages {
        stage('test') {
            agent {
                docker { image 'python:3' 
                         args '-v C:\\Users\\Tal\\.jenkins\\workspace\\World of games - tests'
                       }
            }
            steps {
                sh 'date'
            }
        }
    }
}
