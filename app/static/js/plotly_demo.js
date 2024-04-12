// Install D3.js to help with CSV parsing
// You may need to run 'npm install d3' or similar in your project

// Load the CSV data
d3.csv("/static/js/weather.csv").then((data) => {
  // Prepare the data for Plotly
  const x = data.map((d) => d.date);
  const y = data.map((d) => d.temperature_2m); // Create the Plotly plot

  Plotly.newPlot("myDiv", [
    {
      x: x,
      y: y,
      type: "scatter",
      mode: "lines+markers", // Add lines and markers for better visualization
    },
  ]);
});
 