window.onload = function () {
  var converter = new showdown.Converter();
  fetch("/static/js/text.md")
    .then((response) => response.text())
    .then((text) => {
      var html = converter.makeHtml(text);
      document.getElementById("markdownDiv").innerHTML = html;
    })
    .catch((err) => console.error("Failed to load markdown file:", err));
};
