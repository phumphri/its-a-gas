
var total_sales= [];
var sales = [];
var gdp = [];
var v; 
var trace1
var trace2
var total_car = []
var total_ltruck = []
var auto_dom = []
var ltruck_dom = []
var auto_for = []
var ltruck_for = []
var data = []
var layout
var trace1






var buildplot = function(){  
axios.get('https://its-a-gas.herokuapp.com/sales_rollup')
  .then(function (response) {
    
    
    var sales_json = response.data.table_data
    var ltruck_json_domestic = []
    var ltruck_json_foriegn = []
    var auto_json_domestic = []
    var auto_json_foriegn = []
    var i;
    for(i =0; i < sales_json.length; i = i + 5){
      auto_json_domestic.push(+sales_json[i][2])
    }
    for(i =1; i < sales_json.length; i = i + 5){
      ltruck_json_domestic.push(+sales_json[i][2])
    }
    for(i =2; i < sales_json.length; i = i + 5){
      auto_json_foriegn.push(+sales_json[i][2])
    }
    for(i =3; i < sales_json.length; i = i + 5){
      ltruck_json_foriegn.push(+sales_json[i][2])
    }
   

      ltruck_dom = ltruck_json_domestic.slice(7,)
      ltruck_for = ltruck_json_foriegn.slice(7,)
      auto_dom = auto_json_domestic.slice(7,)
      auto_for = auto_json_foriegn.slice(7,)

    
    var trace1 = {
      x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
      y: ltruck_dom,
      type: "bar",
      name: "Ltruck D Sales"

    };
     var trace2 = {
      x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
      y: ltruck_for,
      type: "bar",
      name: "Ltruck F Sales"

    };
     var trace3 = {
      x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
      y: auto_dom,
      type: "bar",
      name: "Auto D Sales"

    };
     var trace4 = {
      x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
      y: auto_for,
      type: "bar",
      name: "Auto F Sales"

    };
    var trace_oil = {
      x: ['2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
      y: [2.53, 2.25, 2.52, 3.44, 3.58, 3.68, 3.58, 2.84, 2.41, 3.30, 2.84],
      type: "scatter",
      yaxis:"y2",
      name: "Gas",
      line :{color : "black", width : 6}
    };
    var layout = { title: "Car vs. Light Truck Sales in US",
                  barmode: 'stack',
                  yaxis: {title: "Annual Sales in 1000s "},
                  yaxis2: {
                    title: "Gas Price",
                    titlefont: {color: "rgb(148, 103, 189)"},
                    tickfont: {color: "rgb(148, 103, 189)"},
                    overlaying: "y",
                    side: "right"}
                  };
      
    
    var data = [trace1, trace2, trace3, trace4, trace_oil];
    Plotly.plot("plot", data, layout);
  });




  };



buildplot();

