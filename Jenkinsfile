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
                // sh 'sudo -H python3 -m pip install -r requirements.txt --user'
                sh 'echo hello'
                sh '/usr/local/bin/python3 -m pip install --upgrade pip --user'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python'
                }
            }
            steps {
                sh 'python3 -m pip install pytest'
                sh 'python3 -m pytest'
            }
            // post {
            //     always {
            //         junit 'test-reports/results.xml'
            //     }
            // }
        }
        // stage('Deliver') { 
        //     agent {docker{ image 'jcdemo/flaskapp'}}
        //     environment { 
        //         VOLUME = '$(pwd)/sources:/src'
        //         IMAGE = 'cdrx/pyinstaller-linux:python2'
        //     }
        //     steps {
        //         dir(path: env.BUILD_ID) { 
        //             unstash(name: 'compiled-results') 
        //             sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F add2vals.py'" 
        //         }
        //     }
        //     post {
        //         success {
        //             archiveArtifacts "${env.BUILD_ID}/sources/dist/add2vals" 
        //             sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
        //         }
        //     }
        // }
    }
}