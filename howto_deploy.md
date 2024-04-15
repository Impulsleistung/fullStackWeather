### Building and Deploying Your Application on a Linode Kubernetes Cluster

#### Prerequisites

- A Linode account with Kubernetes Cluster set up.
- Docker and Kubernetes CLI (kubectl) installed on your local machine.
- Your local machine configured to interact with your Linode Kubernetes cluster (use `linode-cli k8s` to configure).

#### Step 1: Building the Docker Image

1. Ensure your `Dockerfile` is correctly set up in the project root to package your FastAPI application.
2. Navigate to the root directory of your project.
3. Build your Docker image with the following command:
   ```bash
   docker build -t impulsleistung/weather-app:v1.0 .
   ```
   Replace `<your-docker-username>` with your Docker Hub username.
4. Push the image to your Docker Hub repository:
   ```bash
   docker push impulsleistung/weather-app:v1.0
   ```

#### Step 2: Creating Kubernetes Deployment and Service

1. Edit the `deployment.yaml` and `service.yaml` in your `./k8s` directory to reflect the correct Docker image path.
   - In `deployment.yaml`, change `image: impulsleistung/weather-app:v1.0` to `image: <your-docker-username>/weather-app:v1.0`.
2. Apply the deployment configuration:
   ```bash
   kubectl apply -f ./k8s/deployment.yaml
   ```
3. Apply the service configuration:
   ```bash
   kubectl apply -f ./k8s/service.yaml
   ```

#### Step 3: Accessing Your Application

1. Once deployed, check the status of your deployment:
   ```bash
   kubectl get deployments
   ```
2. Check your service to get the external IP:
   ```bash
   kubectl get services
   ```
   This command will display the external IP under the `EXTERNAL-IP` column, which you can use to access your application via a web browser.

#### Step 4: Managing the Application

- Monitor your application logs:
  ```bash
  kubectl logs -f deployment/<deployment-name>
  ```
- Update the deployment with a new image version:
  ```bash
  kubectl set image deployment/<deployment-name> <container-name>=impulsleistung/weather-app:v1.0
  ```
- Scale your deployment:
  ```bash
  kubectl scale deployment <deployment-name> --replicas=<number-of-replicas>
  ```

#### Optional: Configure Continuous Deployment

- Set up a CI/CD pipeline using GitHub Actions or GitLab CI to automate the build and deployment process every time you make changes to your codebase.

Make sure to replace placeholders with actual names and paths used in your configuration. This guide assumes your Kubernetes files (`deployment.yaml` and `service.yaml`) are set up correctly according to your cluster's requirements.
