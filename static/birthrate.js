
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

d3.json("/birth_rate").then( function(data1){
    console.log(data1);
    var data2 = data1;
    var trace1 = {
    x: data2.map(function(d) {return d.x;}),
    y: data2.map(function(d) {return d.y;}),
    type: "line"
    };
    data3 = [trace1];
    var layout = {
        title: "birth rates 1950-2021"
    };
    Plotly.newPlot('line-chart', data3);
});