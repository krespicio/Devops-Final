pipeline {
    agent { docker { image 'python:3.7.2' } }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m pip install -r requirements.txt --user'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
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