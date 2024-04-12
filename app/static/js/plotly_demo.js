d3.csv("/static/js/weather.csv").then((data) => {
  // Prepare the data for Plotly
  const x = data.map((d) => d.date);
  const temperature = data.map((d) => d.temperature_2m);
  const rain = data.map((d) => d.rain);
  const surfacePressure = data.map((d) => d.surface_pressure);

  // Define a common dark theme layout with white grid lines
  const darkLayout = {
    paper_bgcolor: "#5f7f99", // Dark background for the plot area
    plot_bgcolor: "#5f7f99", // Same as paper background
    font: {
      color: "#FFFFFF", // White font for better visibility
    },
    xaxis: {
      gridcolor: "#FFFFFF", // White grid lines for the x-axis
      zerolinecolor: "#FFFFFF", // White zero line for the x-axis
    },
    yaxis: {
      gridcolor: "#FFFFFF", // White grid lines for the y-axis
      zerolinecolor: "#FFFFFF", // White zero line for the y-axis
    },
    title: {
      font: {
        size: 16,
      },
    },
  };

  // Create the temperature plot with the dark theme
  Plotly.newPlot(
    "temperatureDiv",
    [
      {
        x: x,
        y: temperature,
        type: "scatter",
        mode: "lines+markers",
        name: "Temperature",
        marker: { color: "red" }, // Optional: Adjust marker color for visibility
      },
    ],
    { ...darkLayout, title: "Temperature (°C)" }
  );

  // Create the rain plot with the dark theme
  Plotly.newPlot(
    "rainDiv",
    [
      {
        x: x,
        y: rain,
        type: "scatter",
        mode: "lines+markers",
        name: "Rain",
        marker: { color: "blue" }, // Optional: Adjust marker color for visibility
      },
    ],
    { ...darkLayout, title: "Rain (mm)" }
  );

  // Create the surface pressure plot with the dark theme
  Plotly.newPlot(
    "pressureDiv",
    [
      {
        x: x,
        y: surfacePressure,
        type: "scatter",
        mode: "lines+markers",
        name: "Surface Pressure",
        marker: { color: "green" }, // Optional: Adjust marker color for visibility
      },
    ],
    { ...darkLayout, title: "Surface Pressure (hPa)" }
  );
});
