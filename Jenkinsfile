pipeline {
    agent { docker { image 'python:3.7.2' } }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'sudo -H pip install flask'
                sh 'sudo -H pip install pytest'
                sh 'export FLASK_APP=flaskr'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
            // post {
            //     always {
            //         junit 'test-reports/results.xml'
            //     }
            // }
        }
        // stage('Deliver') { 
        //     agent any
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