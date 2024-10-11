pipeline {
    agent any
    
    stages {
        stage('Fetch Code') {
            steps {
                git branch: 'main', url: 'https://github.com/timucinozkan/rpg_game.git'
            }
        }
        stage('Code Analysis') {
            environment {
                scannerHome = tool 'Sonar'
            }
            steps {
                script {
                    withSonarQubeEnv(credentialsId: 'sonar-rpg_game', installationName: 'Sonar') {
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=jenkinsfile-sonar \
                            -Dsonar.sources=. \
                            -Dsonar.python.version=3"
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