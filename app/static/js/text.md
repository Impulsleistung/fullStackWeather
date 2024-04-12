This full stack project is a weather visualization web application built using FastAPI, JavaScript, Plotly, and Docker, hosted in a Kubernetes environment.
_Built by [Kevin Ostheimer](http://www.impulsleistung.de), 2024._

**Backend Application (FastAPI):** The backend, written in Python using FastAPI, manages periodic tasks that fetch and process weather data using an Open-Meteo API client. __City: Pforzheim, Germany.__

**Frontend Visualization:** The frontend utilizes Plotly and D3.js to visualize weather data (temperature, rain, surface pressure) from the updated CSV file.

**Web Interface:** An HTML page serves as the interface where users can view these visualizations in different plots.

**Data Management:** The application uses caching and retry mechanisms for API requests to ensure data reliability and availability.

**Deployment and Service:** The application is containerized using Docker and deployed using Kubernetes, allowing for scalable and robust hosting.