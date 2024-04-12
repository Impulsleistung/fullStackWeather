To run and inspect your Docker container locally, follow these steps using Docker commands in your terminal. Here’s how you can do it:

### Step 1: Build the Docker Image

```bash
docker build -t weather-app:local .
```

This command builds an image and tags it as `weather-app:local`. Ensure your Dockerfile and all necessary files are correctly placed in the project directory.

### Step 2: Run the Docker Container
After building the image, run the container:

```bash
docker run -d --name weather-app-container -p 8000:8000 weather-app:local
```

Here’s what this command does:
- `-d`: Runs the container in detached mode (in the background).
- `--name weather-app-container`: Assigns the container a name.
- `-p 8000:8000`: Maps port 8000 of the container to port 8000 on your host. This allows you to access the FastAPI application via `localhost:8000` in your browser.

### Step 3: Inspect the Container
To inspect various aspects of the running container, you can use several Docker commands:

#### View Logs
To see the logs from your container (which is useful for debugging), use:

```bash
docker logs weather-app-container
```

#### Check Running Processes
To see the processes running inside the container:

```bash
docker top weather-app-container
```

#### Inspect Container Configuration
For more detailed information about the container's configuration and environment:

```bash
docker inspect weather-app-container
```

#### Access Container’s Shell
If you need to enter the container to explore its contents or debug it interactively:

```bash
docker exec -it weather-app-container /bin/bash
```

This command opens a bash shell inside the container. If the container does not include bash, you might need to use `/bin/sh` instead.

#### Monitoring Container Performance
To monitor the real-time performance of your container, use:

```bash
docker stats weather-app-container
```

### Step 4: Stop and Remove the Container
When you're done, you can stop the container:

```bash
docker stop weather-app-container
```

And if you wish to remove it:

```bash
docker rm weather-app-container
```

These steps will help you run, test, and inspect your Docker container locally. Make sure each step completes without errors to ensure your application is functioning as expected inside Docker.