# Full Stack Weather App

The full-stack project is a weather visualization web application built using FastAPI, JavaScript, Plotly, and Docker, hosted in a Kubernetes environment.

![result](/docs/browser_screenshot.jpg)

Here are the key functionalities and components:

1. **Backend Application (FastAPI):**

   - The backend, written in Python using FastAPI, manages periodic tasks that fetch and process weather data using an Open-Meteo API client.
   - Weather data for specific geographic coordinates is obtained, processed, and saved to a CSV file periodically (every 10 minutes).

2. **Frontend Visualization:**

   - The frontend utilizes Plotly and D3.js to visualize weather data (temperature, rain, surface pressure) from the updated CSV file.
   - JavaScript functions fetch and convert data into graphical plots displayed in a web interface.

3. **Web Interface:**

   - An HTML page serves as the interface where users can view these visualizations in different plots.
   - Markdown content is dynamically loaded and converted to HTML, providing additional information or descriptions on the webpage.

4. **Data Management:**

   - The application uses caching and retry mechanisms for API requests to ensure data reliability and availability.

5. **Deployment and Service:**
   - The application is containerized using Docker and deployed using Kubernetes, allowing for scalable and robust hosting.
   - It includes configurations for a load-balanced service to manage traffic to multiple instances of the application.

_Built by Kevin Ostheimer, 2024_
