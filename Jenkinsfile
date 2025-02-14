pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('vaishnavi7009_dockerhub')
        GIT_REPO = 'https://github.com/Decode777/assess2_jenk.git'
        DOCKER_IMAGE = 'vaishnavi7009/your-flask-app'
    }

    stages {
        // Stage 1: Checkout Code
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: env.GIT_REPO
            }
        }

        // Stage 2: Build Docker Image
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(env.DOCKER_IMAGE)
                }
            }
        }

        // Stage 3: Run Tests
        stage('Run Tests') {
    steps {
        script {
            docker.image(env.DOCKER_IMAGE).inside('-v /c/ProgramData/Jenkins/.jenkins/workspace/Flask-App-Pipeline:/app') {
                sh 'python -m pytest /app/tests/'
            }
        }
    }
}

        // Stage 4: Push Image to Docker Hub
        stage('Push Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', env.DOCKER_HUB_CREDENTIALS) {
                        docker.image(env.DOCKER_IMAGE).push('latest')
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