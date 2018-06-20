
var total_sales= [];
var sales = [];
var gdp = [];
var v; 
var trace1
var trace2
var total_car = []
var total_ltruck = []
var car = []
var ltruck = []
var data = []
var layout



var getData = function(callback){
axios.get('https://its-a-gas.herokuapp.com/gdp')
  .then(function (response) {
    
    var gdp_json  = response.data.table_data;
    var i;
    for(i = 0; i < gdp_json.length; i++){
      gdp.push(gdp_json[i][1]);
    }
    trace2 = {
      x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
      y: gdp,
      type: "scatter",
      yaxis:"y2",
      name: "GDP"
    };
  });
  callback();
}




var buildplot = function(){  
axios.get('https://its-a-gas.herokuapp.com/sales_rollup')
  .then(function (response) {
    
    
    var sales_json = response.data.table_data
    var i;
    for(i =4; i < sales_json.length; i = i + 5){
      total_sales.push(+sales_json[i][2])
    }
    for(i =0; i < sales_json.length; i = i + 5){
      total_car.push(+sales_json[i][2])
    }
    for(i =1; i < sales_json.length; i = i + 5){
      total_ltruck.push(+sales_json[i][2])
    }
    sales = total_sales.slice(7,)
    car = total_car.slice(7,)
    ltruck = total_ltruck.slice(7,)

    console.log(sales)
    var trace1 = {
      x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
      y: sales,
      type: "scatter",
      name: "Auto Sales"

    };
    var layout = {
      title: "Total Auto Sales in US",
      titlefont: {
        size: 36
      },
      yaxis: {title: "Annual Auto Sales in 1000s "},
      yaxis2: {
        title: "Annual GDP in Trillions",
        titlefont: {color: "rgb(148, 103, 189)", },
        tickfont: {color: "rgb(148, 103, 189)"},
        overlaying: "y",
        side: "right",
        
      }
      
    };
    var data = [trace1, trace2];
    Plotly.plot("plot", data, layout);


    var bar1 = {
      x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
      y: ltruck,
      name: 'Domestic Light Truck',
      type: 'bar'
    };
    
    var bar2 = {
      x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
      y: car,
      name: 'Domestic Car',
      type: 'bar'
    };

    var trace_oil = {
      x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
      y: [2.53, 2.25, 2.52, 3.44, 3.58, 3.68, 3.58, 2.84, 2.41, 3.30, 2.84],
      type: "scatter",
      yaxis:"y2",
      name: "Oil",
      line :{color : "black", width : 6}
    };
    
    var data = [bar1, bar2, trace_oil];
    
    var layout = { title: "Car vs. Light Truck Sales in US",
                  titlefont: {
                    size: 36
                  },
                  barmode: 'group',
                  yaxis: {title: "Annual Sales in 1000s "},
                  yaxis2: {
                    title: "Gasoline Price per Gallon",
                    titlefont: {color: "rgb(148, 103, 189)"},
                    tickfont: {color: "rgb(148, 103, 189)"},
                    overlaying: "y",
                    side: "right"}
                  };
    
    Plotly.plot("plot2", data, layout);

  });


}


getData(function(){buildplot()});

Plotly.d3.select("#Option2").on("click",function(){
  var trace1 = {
    x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
    y: sales,
    type: "scatter",
    name: "Auto Sales"

  };
  var trace_oil = {
    x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
    y: [2.53, 2.25, 2.52, 3.44, 3.58, 3.68, 3.58, 2.84, 2.41, 3.30, 2.84],
    type: "scatter",
    yaxis:"y2",
    name: "Oil",
    line :{color : "black", width : 6}
  };
  data = [trace1, trace_oil]

  var layout = { title: "Total Auto Sales in US" ,
                  titlefont: {
                    size: 36
                  },
                  yaxis: {title: "Annual Auto Sales in 1000s "},
                  yaxis2: {
                    title: "Gasoline Price per Gallon",
                    titlefont: {color: "rgb(148, 103, 189)"},
                    tickfont: {color: "rgb(148, 103, 189)"},
                    overlaying: "y",
                    side: "right"}
                  };
  
  Plotly.newPlot("plot", data, layout);
})


Plotly.d3.select("#Option1").on("click",function(){
var trace1 = {
  x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
  y: sales,
  type: "scatter",
  name: "Auto Sales"

};
var trace2 = {
  x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
  y: gdp,
  type: "scatter",
  yaxis:"y2",
  name: "GDP"
};
var layout = {
  title: "Total Auto Sales in US",
  titlefont: {
    size: 36
  },
  yaxis: {title: "Annual Auto Sales in 1000s "},
  yaxis2: {
    title: "Annual GDP in Trillions",
    titlefont: {color: "rgb(148, 103, 189)"},
    tickfont: {color: "rgb(148, 103, 189)"},
    overlaying: "y",
    side: "right",
    
  }
  
};
var data = [trace1, trace2];
Plotly.newPlot("plot", data, layout);
})

Plotly.d3.select("#Option1_bar").on("click",function(){
  var bar1 = {
    x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
    y: ltruck,
    name: 'Domestic Light Truck',
    type: 'bar'
  };
  
  var bar2 = {
    x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
    y: car,
    name: 'Domestic Car',
    type: 'bar'
  };

  var trace_gdp = {
  
      x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
      y: gdp,
      type: "scatter",
      yaxis:"y2",
      name: "GDP"
    
  };

  var data = [bar1, bar2, trace_gdp];
    
    var layout = { title: "Car vs. Light Truck Sales in US",
                    titlefont: {
                      size: 36
                    },
                  barmode: 'group',
                  yaxis: {title: "Annual Sales in 1000s "},
                  yaxis2: {
                    title: "GDP (Trillions)",
                    titlefont: {color: "rgb(148, 103, 189)"},
                    tickfont: {color: "rgb(148, 103, 189)"},
                    overlaying: "y",
                    side: "right"}
                  };
  
  Plotly.newPlot("plot2", data, layout);
})

Plotly.d3.select("#Option2_bar").on("click",function(){
  var bar1 = {
    x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
    y: ltruck,
    name: 'Domestic Light Truck',
    type: 'bar'
  };
  
  var bar2 = {
    x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
    y: car,
    name: 'Domestic Car',
    type: 'bar'
  };

  var trace_oil = {
    x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
    y: [2.53, 2.25, 2.52, 3.44, 3.58, 3.68, 3.58, 2.84, 2.41, 3.30, 2.84],
    type: "scatter",
    yaxis:"y2",
    name: "Oil",
    line :{color : "black", width : 6}
  };
    
  ;

  var data = [bar1, bar2, trace_oil];
    

  var layout = { title: "Car vs. Light Truck Sales in US",
                  titlefont: {
                    size: 36
                  },
                  barmode: 'group',
                  yaxis: {title: "Annual Sales in 1000s "},
                  yaxis2: {
                    title: "Gasoline Price per Gallon ",
                    titlefont: {color: "rgb(148, 103, 189)"},
                    tickfont: {color: "rgb(148, 103, 189)"},
                    overlaying: "y",
                    side: "right"}
                  };
  
  Plotly.newPlot("plot2", data, layout);
})