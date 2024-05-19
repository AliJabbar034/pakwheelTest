pipeline {
    agent any

    environment {
        CHROME_BIN = "/usr/bin/google-chrome"
        CHROME_DRIVER = "/usr/local/bin/chromedriver"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/AliJabbar034/pakwheelTest.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --html=report.html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            publishHTML(target: [
                reportName: 'HTML Report', 
                reportDir: '.', 
                reportFiles: 'report.html'
            ])
        }
    }
}
