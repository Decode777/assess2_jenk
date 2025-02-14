pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('vaishnavi7009_dockerhub')
        GIT_REPO = 'https://github.com/Decode777/assess2_jenk.git'
        DOCKER_IMAGE = 'vaishnavi7009/your-flask-app'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: env.GIT_REPO
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("${env.DOCKER_IMAGE}:${env.BUILD_ID}").inside('--workdir /app') {
                        sh 'pytest test_routes.py'
                    }
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', env.DOCKER_HUB_CREDENTIALS) {
                        docker.image("${env.DOCKER_IMAGE}:${env.BUILD_ID}").push()
                        docker.image("${env.DOCKER_IMAGE}:${env.BUILD_ID}").push('latest')
                    }
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
