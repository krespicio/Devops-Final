pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
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
                    sh 'python3 -m pytest'
                }
            }
        }
        stage('Deliver') { 
            agent any
            environment { 
                VOLUME = '$(pwd)/flaskr' // This is where the project belongs
                IMAGE = 'jcdemo/flaskapp'
            }
            steps {
                // withEnv(["HOME=${env.WORKSPACE}"]) {
                sh "pwd"
                sh "echo ${VOLUME}"
                sh "docker run -d --rm -v ${VOLUME} ${IMAGE} -p 56733:5000" 
                // }
            }
            post {
                success {
                    sh 'echo wow'
                    // sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}