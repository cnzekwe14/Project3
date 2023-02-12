
d3.json("/births").then( function(data){
    var data1 = data;
    var trace = {
    x: data1.map(function(d) {return d.x}),
    y: data1.map(function(d) {return d.y}),
    type: "bar"
    };
    data2 = [trace];
    var layout = {
        title: "birth rates"
    };
    Plotly.newPlot('bar', data2);
});
