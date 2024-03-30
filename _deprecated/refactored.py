import json
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import AutoMinorLocator  # Corrected import
from datetime import datetime
import mpld3
import base64


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


import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import matplotlib.dates as mdates
from datetime import datetime
import mpld3
import base64
import pandas as pd
import base64  # Ensure this import is at the top of your script


def export_plot_to_html(fig):
    """
    Exports the given matplotlib figure to an HTML file, embedding the plot as a base64 image.

    Parameters:
    - fig: The matplotlib figure to export.
    """
    plt.savefig("data/weather_plot.jpg", format="jpg")
    plt.close(fig)  # Close the plot to free memory

    # Encode the saved image to base64
    with open("data/weather_plot.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

    # Embed the JPG in an HTML file
    html_template = f"""
    <html>
    <head>
    <title>Pforzheim Weather</title>
    <style>
        body {{
            background-color: black;
            color: white;
        }}
    </style>
    </head>
    <body>
    <img src="data:image/jpg;base64,{encoded_string}" alt="Pforzheim Weather">
    </body>
    </html>
    """

    # Write the HTML to a file
    with open("data/weather_plot.html", "w") as f:
        f.write(html_template)


def plot_weather_data(df, export_html=False):
    """
    Plots the weather data from the DataFrame using a dark theme, adds a high-contrast grid to the plots,
    marks the current time with a vertical line, assigns a different color to each plot,
    and shows the current time as the label of the marker. Minor ticks are added to the grid for better granularity.

    Parameters:
    - df: DataFrame containing weather data.
    - export_html: If True, exports the plot as an HTML file embedded with the plot image.
    """
    # Use dark background theme
    plt.style.use("dark_background")

    fig, axs = plt.subplots(nrows=len(df.columns) - 1, ncols=1, figsize=(10, 8))

    # Define high contrast colors
    colors = ["cyan", "magenta", "yellow", "white", "red", "green", "blue"]
    current_time = pd.to_datetime(datetime.now(), utc=True)
    current_time_str = current_time.strftime("%H:%M UTC")
    closest_date = df.iloc[(df["date"] - current_time).abs().argsort()[0]]["date"]

    for i, var in enumerate(df.columns[1:]):
        color = colors[i % len(colors)]
        axs[i].plot(
            df["date"],
            df[var],
            label=var,
            color=color,
            marker="o",
            markersize=3,
            linestyle="-",
        )
        axs[i].set_title(var)
        axs[i].legend()

        # Set grid and add minor ticks
        axs[i].grid(True, which="both", linestyle="--", linewidth=0.5)

        # Mark the current time
        axs[i].axvline(
            x=closest_date,
            color="r",
            linestyle="--",
            label=f"Current Time: {current_time_str}",
        )
        axs[i].legend()

    plt.tight_layout()
    export_plot_to_html(fig)


def save_data_as_json(data, filename="data/weather.json"):
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


# Usage Example
openmeteo_client = setup_openmeteo_api_client()
weather_df = fetch_and_process_weather_data(
    openmeteo_client,
    latitude=48.8844,
    longitude=8.6989,
    variables=["temperature_2m", "rain", "surface_pressure"],
    past_days=3,
    forecast_days=3,
)
print(weather_df.head())  # Displaying a part of the DataFrame for verification
plot_weather_data(weather_df, export_html=True)
save_data_as_json(weather_df)
