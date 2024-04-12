import json
import openmeteo_requests
import requests_cache
from retry_requests import retry
import pandas as pd


def setup_openmeteo_api_client():
    """
    Sets up the Open-Meteo API client with caching and retry mechanisms.
    Returns an Open-Meteo client object.
    """
    cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo_client = openmeteo_requests.Client(session=retry_session)
    return openmeteo_client


def fetch_and_process_weather_data(
    client, latitude, longitude, variables, past_days, forecast_days
):
    """
    Fetches and processes weather data for a given location.

    Parameters:
    - client: Open-Meteo client object.
    - latitude: Latitude of the location.
    - longitude: Longitude of the location.
    - variables: List of weather variables to fetch.
    - past_days: Number of past days to fetch data for.
    - forecast_days: Number of forecast days to fetch data for.

    Returns a DataFrame containing the weather data.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": variables,
        "past_days": past_days,
        "forecast_days": forecast_days,
    }
    response = client.weather_api(url, params=params)[
        0
    ]  # Assuming single location for simplicity
    hourly = response.Hourly()

    hourly_data = {
        "date": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left",
        )
    }
    for i, variable in enumerate(variables):
        hourly_data[variable] = hourly.Variables(i).ValuesAsNumpy()

    return pd.DataFrame(data=hourly_data)

# C:\Users\info\Desktop\fullStackWeather\app\static\js\demo_data.json
def save_data_as_json(data, filename="app/static/js/weather.json"):
    """
    Saves the given data in a JSON file.

    Parameters:
    - data: Pandas DataFrame containing the weather data.
    - filename: The path and name of the file where the data will be saved.
    """
    # Convert the pandas DataFrame to a JSON string
    json_str = data.to_json(orient="records")

    # Write the JSON string to a file
    with open(filename, "w") as file:
        file.write(json_str)

    print(f"Data successfully saved to {filename}.")


def execute_something():
    # Usage Example
    openmeteo_client = setup_openmeteo_api_client()
    weather_df = fetch_and_process_weather_data(
        openmeteo_client,
        latitude=48.8844,  # Replace with your latitude
        longitude=8.6989,  # Replace with your longitude
        variables=["temperature_2m", "rain", "surface_pressure"],
        past_days=3,
        forecast_days=3,
    )
    save_data_as_json(weather_df)
    print(weather_df.head())  # Displaying a part of the DataFrame for verification
