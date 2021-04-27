pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        // Set up the python environment
        stage('Build') {
            agent {
                docker {
                    image 'python'
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                }
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python'
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python3 coverage run -m pytest'
                    sh 'python3 -m coverage report'
                }
            }
        }
        // Deploy the app
        stage('Deliver') { 
            agent any
            environment { 
                VOLUME = '$(pwd)/flaskr' // This is where the project belongs
                IMAGE = 'jcdemo/flaskapp' // May want to change docker image later...
            }
            steps {
                sh "docker run -d --rm -v ${VOLUME} ${IMAGE} -p 56733:5000" 
            }
            post {
                success {
                    sh "docker run -d --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}