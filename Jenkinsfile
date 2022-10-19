pipeline {
    agent any

    stages {
        stage("build") {
            when {
                expression {
                    BRANCH_NAME == 'gke' || BRANCH_NAME == 'main'
                }
            }
            steps {
                echo 'building'
                ls ./
                echo PWD
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