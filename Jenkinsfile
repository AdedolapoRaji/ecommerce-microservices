pipeline {
    agent any
    
    environment {
        // Your Docker Hub username
        DOCKER_USER = 'adedolapo05'
        // Securely loads the secret token from Jenkins credentials manager
        DOCKER_HUB_TOKEN = credentials('dockerhub-token') 
    }

    stages {
        stage('Step 1: Checkout Source Code') {
            steps {
                // This ensures Jenkins has the latest files in your workspace
                checkout scm
            }
        }

        stage('Step 2: Login to Docker Hub') {
            steps {
                // Log in securely using stdout masking
                sh "echo \$DOCKER_HUB_TOKEN | docker login -u \$DOCKER_USER --password-stdin"
            }
        }

        stage('Step 3: Build, Tag, & Push Modules') {
            steps {
                script {
                    // Loop through all four of your service folders
                    def modules = ['product', 'cart', 'order', 'notification']
                    
                    for (module in modules) {
                        echo "--------------------------------------------------"
                        echo "PROCESSING MODULE: ${module}-service"
                        echo "--------------------------------------------------"
                        
                        # 1. Build the local image using the directory's Dockerfile
                        sh "docker build -t ${DOCKER_USER}/ecommerce-${module}:latest ./${module}-service"
                        
                        # 2. Push the tagged image directly to your Docker Hub
                        sh "docker push ${DOCKER_USER}/ecommerce-${module}:latest"
                    }
                }
            }
        }
        
        stage('Step 4: Post-Build Cleanup') {
            steps {
                // Cleans up dangling build layers on your manager node to save space
                sh "docker image prune -f"
                echo "All images pushed to Docker Hub successfully!"
            }
        }
    }
}
