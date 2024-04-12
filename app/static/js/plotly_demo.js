// Install D3.js to help with CSV parsing
// Load the CSV data

d3.csv("/static/js/weather.csv").then((data) => {
  // Prepare the data for Plotly
  const x = data.map((d) => d.date);
  const temperature = data.map((d) => d.temperature_2m);
  const rain = data.map((d) => d.rain);
  const surfacePressure = data.map((d) => d.surface_pressure);

  // Create the temperature plot
  Plotly.newPlot(
    "temperatureDiv",
    [
      {
        x: x,
        y: temperature,
        type: "scatter",
        mode: "lines+markers",
        name: "Temperature",
      },
    ],
    {
      title: "Temperature (°C)",
    }
  );

  // Create the rain plot
  Plotly.newPlot(
    "rainDiv",
    [
      {
        x: x,
        y: rain,
        type: "scatter",
        mode: "lines+markers",
        name: "Rain",
      },
    ],
    {
      title: "Rain (mm)",
    }
  );

  // Create the surface pressure plot
  Plotly.newPlot(
    "pressureDiv",
    [
      {
        x: x,
        y: surfacePressure,
        type: "scatter",
        mode: "lines+markers",
        name: "Surface Pressure",
      },
    ],
    {
      title: "Surface Pressure (hPa)",
    }
  );
});
