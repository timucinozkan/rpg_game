pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    // Check out the main branch from the repository
                    checkout([$class: 'GitSCM',
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[url: 'https://github.com/timucinozkan/rpg_game.git']]
                        ])
                }
            }
        }
        stage('Code Analysis') {
            environment {
                scannerHome = tool 'Sonar'
            }
            steps {
                script {
                    // sources: path to analyze, projectKey: sonar project name
                    withSonarQubeEnv(credentialsId: 'sonar-rpg_game', installationName: 'Sonar') {
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=jenkinsfile-sonar \
                            -Dsonar.sources=. \
                            -Dsonar.python.version=3"
                    }
                }
            }
        }
        stage('Quality Gate'){
            steps{
                script{
                    timeout(time: 3, unit:'MINUTES'){
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error 'Pipeline aborted: ${qg.status}'
                        }
                    }
                }
            }
        }
    }
    post {
        // Clean after build
        always {
            cleanWs(cleanWhenNotBuilt: false,
                    deleteDirs: true,
                    disableDeferredWipeout: true,
                    notFailBuild: true,
                    patterns: [[pattern: '.gitignore', type: 'INCLUDE'],
                               [pattern: '.propsfile', type: 'EXCLUDE']])
        }
    }
}