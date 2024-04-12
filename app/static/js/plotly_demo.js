d3.csv("/static/js/weather.csv").then((data) => {
  // Prepare the data for Plotly
  const x = data.map((d) => d.date);
  const temperature = data.map((d) => d.temperature_2m);
  const rain = data.map((d) => d.rain);
  const surfacePressure = data.map((d) => d.surface_pressure);

  // Define a common dark theme layout with white grid lines and zero margins
  const darkLayout = {
    margin: { l: 20, r: 20, t: 10, b: 50 }, // Zero margins
    paper_padding: 1,
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
        marker: { color: "red" },
      },
    ],
    {
      ...darkLayout,
      yaxis: { title: "Temperature (°C)", automargin: true }, // Y-axis label added with auto margin
    }
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
        marker: { color: "blue" },
      },
    ],
    {
      ...darkLayout,
      yaxis: { title: "Rain (mm)", automargin: true }, // Y-axis label added with auto margin
    }
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
        marker: { color: "green" },
      },
    ],
    {
      ...darkLayout,
      yaxis: { title: "Surface Pressure (hPa)", automargin: true }, // Y-axis label added with auto margin
    }
  );
});
