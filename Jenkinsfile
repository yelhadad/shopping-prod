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

    post {
        always {
            echo 'this runs always'
        }

        success {
            echo 'this runs on success'
        }

        failure {
            echo 'this runs on failure'
        }
    }
}