// setting dimensions of canvas
var margin = {top: 30, right: 40, bottom: 50, left: 60},
    width = 800 - margin.left - margin.right,
    height = 800 - margin.bottom - margin.top;

// actual svg
var svg = d3.select(".svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// actual data stuff

