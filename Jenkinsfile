pipeline {
    agent any

    stages {
        stage("build") {
            steps {
                sh 'ls'
                sh 'pwd'
            }
        }

        stage ("test") {
            steps {
                echo 'testing'
            }
        }
        stage ("deploy") {
            steps {
                echo 'deploy'
            }
        }
    }
}