var svg = d3.select("svg"),
    g = svg.append("g");

var clrScreen = function() {
    while (svg.firstChild) {
	svg.removeChild(svg.firstChild);
    }
}

function circle(x,y) {
    var circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx",x);
    circle.setAttribute("cy",y);
    circle.setAttribute("r","20");
    return circle;
}

var draw = function(e) {
    var c = circle(e.offsetX, e.offsetY);
    svg.appendChild(c);
}


svg.addEventListener("click",draw);
