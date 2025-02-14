pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('vaishnavi7009_dockerhub')
        DOCKER_IMAGE = 'vaishnavi7009/flask-app'
    }

    stages {
        // Stage 1: Checkout Code
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Decode777/assess2_jenk.git'
            }
        }

        // Stage 2: Build Docker Image
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        // Stage 3: Run Tests
        stage('Run Tests') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").inside {
                        bat 'python -m pytest tests/'
                    }
                }
            }
        }

        // Stage 4: Push Image to Docker Hub
        stage('Push Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'vaishnavi7009_dockerhub') {
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push()
                    }
                }
            }
        }

        // Stage 5: Deploy Application
        stage('Deploy Application') {
            steps {
                sshagent(['remote-server-credentials']) {
                    bat """
                        powershell -Command "& { ssh -o StrictHostKeyChecking=no user@remote-server 'docker-compose down && docker-compose pull && docker-compose up -d' }"
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
