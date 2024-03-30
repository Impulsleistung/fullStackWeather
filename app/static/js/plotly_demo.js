// Fetch the JSON data
fetch("/static/js/demo_data.json")
  .then((response) => response.json())
  .then((data) => {
    // Use the loaded data for the Plotly plot
    Plotly.newPlot("myDiv", [
      {
        x: data.x,
        y: data.y,
        type: "scatter", // Example of specifying a plot type
      },
    ]);
  });
