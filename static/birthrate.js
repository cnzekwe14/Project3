
d3.json("/births").then( function(data){
    var data1 = data;
    var trace = {
    x: data1.map(function(d) {return d.x}),
    y: data1.map(function(d) {return d.y}),
    type: "bar",
    marker:{
        color: 'green'
    }
    
    };
    data2 = [trace];
    var layout = {
        title: "Average Fertility Rate by Year 2014-2020",
        xaxis: {
            title: 'Year',
            showgrid: false,
            zeroline: false
          },
          yaxis: {
            title: 'Fertility Rate',
            showline: false
          }
        };
    Plotly.newPlot('bar', data2, layout);
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
        title: "Birth Rates 1950-2021",
        xaxis: {
            title: 'Year',
            showgrid: false,
            zeroline: false
          },
          yaxis: {
            title: 'Births',
            showline: false
          }
        };
    
    Plotly.newPlot('line-chart', data3,layout);
});

d3.json("/birth_map").then(function (data) {
    var data3 = data;
    var trace1 = [{
      type: 'choropleth',
      locationmode: 'USA-states',
      z: data3.map(function (d) { return d.x }),
      locations: data3.map(function (d) { return d.y }),
      colorscale: [
        [0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'],
        [0.4, 'rgb(188,189,220)'], [0.6, 'rgb(158,154,200)'],
        [0.8, 'rgb(117,107,177)'], [1, 'rgb(84,39,143)']
      ],
      colorbar: {
        title: 'Fertility Rate',
        thickness: 0.2
      },
      marker: {
        line: {
          color: 'rgb(255,255,255)',
          width: 2
        }
      }
    }];
    
    var layout = {
      title: 'Fertility Rate By State 2020',
      geo: {
        scope: 'usa',
        showlakes: true,
        lakecolor: 'rgb(255,255,255)'
      }
      };
      Plotly.newPlot("map", trace1, layout, { showLink: false });
  });

// let states1 = d3.select("#selDataset");
// d3.json("/drop1").then(function(items){
//     var states = items.map(function(p) {return p.y});
//     for (let state of states){
//         states1.append("option").property("value",state).text(state)
//     };
