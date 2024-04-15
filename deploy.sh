#!/bin/bash

# ./deploy.sh <your-docker-username> <image-version> <deployment-name> <number-of-replicas>

# Define parameters
DOCKER_USERNAME="$1"
IMAGE_VERSION="$2"
DEPLOYMENT_NAME="$3"
REPLICAS="$4"

# Set default values if not provided
if [ -z "$DOCKER_USERNAME" ]; then
  echo "Docker username is required."
  exit 1
fi

if [ -z "$IMAGE_VERSION" ]; then
  IMAGE_VERSION="v1"
fi

if [ -z "$DEPLOYMENT_NAME" ]; then
  DEPLOYMENT_NAME="weather-app-deployment"
fi

if [ -z "$REPLICAS" ]; then
  REPLICAS=2
fi

# Build Docker image
echo "Building Docker image..."
docker build -t ${DOCKER_USERNAME}/weather-app:${IMAGE_VERSION} .

# Push Docker image to repository
echo "Pushing Docker image to Docker Hub..."
docker push ${DOCKER_USERNAME}/weather-app:${IMAGE_VERSION}

# Update Kubernetes deployment and service manifests
sed -i "s|image: .*/weather-app:.*|image: ${DOCKER_USERNAME}/weather-app:${IMAGE_VERSION}|" ./k8s/deployment.yaml

# Apply Kubernetes configurations
echo "Deploying to Kubernetes..."
kubectl apply -f ./k8s/deployment.yaml
kubectl apply -f ./k8s/service.yaml

# Scale the deployment
echo "Scaling the deployment..."
kubectl scale deployment ${DEPLOYMENT_NAME} --replicas=${REPLICAS}

# Wait and get the service with external IP
echo "Retrieving service details..."
sleep 10 # Wait for the service to be available
kubectl get services

echo "Deployment completed. Check above for the external IP to access your application."
