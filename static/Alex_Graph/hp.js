//This file lets the user graph and explore horsepower data from our data set


var brands = ["GMC", "BMW", "Nissan", "Honda", "Volkswagen", "Ford", "Audi", "Ferrari", "Kia", "Mazda", "Maserati", "Subaru", "Volvo", "Lamborghini", "Tesla"]
var sales = [];
var _2008 = [];
var _2009 = [];
var _2010 = [];
var _2011 = [];
var _2012 = [];
var _2013 = [];
var _2014 = [];
var _2015 = [];
var _2016 = [];
var _2017 = [];

var GMC= []
var BMW = []
var Nissan= []
var Honda= []
var Volkswagen = []
var Ford = []
var Audi = []
var Ferrari= []
var Kia =[]
var Mazda = []
var Maserati = []
var Subaru = []
var Volvo = []
var Lamborghini = []
var Tesla = [] 
var Brand_Obj = {}

const average = arr => arr.reduce( ( p, c ) => p + c, 0 ) / arr.length


//request manufacturer data set from API and divide data into list of car brands

axios.get('https://its-a-gas.herokuapp.com/manufacturer')
  .then(function (response) {
    
    var manu_json  = response.data.table_data;
    console.log(response.data)

    for(i = 0; i < manu_json.length; i++){
      if (manu_json[i][1] == "GMC"){
        GMC.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "BMW"){
        BMW.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Nissan"){
        Nissan.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Honda"){
        Honda.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Volkswagen"){
        Volkswagen.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Ford"){
        Ford.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Audi"){
        Audi.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Ferrari"){
        Ferrari.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Kia"){
        Kia.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Mazda"){
        Mazda.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Maserati"){
        Maserati.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Subaru"){
        Subaru.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Volvo"){
        Volvo.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Lamborghini"){
        Lamborghini.push(manu_json[i]);
      }
      else if (manu_json[i][1] == "Tesla"){
        Tesla.push(manu_json[i]);
      }
      else{
        console.log("error")
      }
    }
    

  // create an object for the brands

    Brand_Obj = {GMC :GMC, BMW: BMW, Nissan: Nissan, Honda: Honda,  Volkswagen:Volkswagen, Ford:Ford, Audi:Audi, Ferrari:Ferrari, Kia: Kia, Mazda: Mazda, Maserati:Maserati, Subaru:Subaru, Volvo:Volvo,Lamborghini:Lamborghini, Tesla:Tesla}
    Generate_HP_Graph("Audi")
    
  })
    

  //This function is called to graph the horsepower data for each branch

  Generate_HP_Graph = function(car_brand){

    manu_json = Brand_Obj[car_brand]

    var _2008 = [];
    var _2009 = [];
    var _2010 = [];
    var _2011 = [];
    var _2012 = [];
    var _2013 = [];
    var _2014 = [];
    var _2015 = [];
    var _2016 = [];
    var _2017 = [];
    var years = []

    var i;
    for(i = 0; i < manu_json.length; i++){
      if (+manu_json[i][4] == 2008){
        _2008.push(+manu_json[i][11]);
        years.push(2008)
      }
      else if (+manu_json[i][4] == 2009){
        _2009.push(+manu_json[i][11]);
        years.push(2009)
      }
      else if (+manu_json[i][4] == 2010){
        _2010.push(+manu_json[i][11]);
        years.push(2010)
      }
      else if (+manu_json[i][4] == 2011){
        _2011.push(+manu_json[i][11]);
        years.push(2011)
      }
      else if (+manu_json[i][4] == 2012){
        _2012.push(+manu_json[i][11]);
        years.push(2012)
      }
      else if (+manu_json[i][4] == 2013){
        _2013.push(+manu_json[i][11]);
        years.push(2013)
      }
      else if (+manu_json[i][4] == 2014){
        _2014.push(+manu_json[i][11]);
        years.push(2014)
      }
      else if (+manu_json[i][4] == 2015){
        _2015.push(+manu_json[i][11]);
        years.push(2015)
      }
      else if (+manu_json[i][4] == 2016){
        _2016.push(+manu_json[i][11]);
        years.push(2016)
      }
      else if (+manu_json[i][4] == 2017){
        _2017.push(+manu_json[i][11]);
        years.push(2017)
      }
      else{
        console.log("error")
      }
    }
    var HP = [average(_2008),average(_2009),average(_2010),average(_2011),average(_2012),average(_2013),average(_2014),average(_2015),average(_2016),average(_2017) ];
    

    var unique_years = years.filter((v, i, a) => a.indexOf(v) === i);
    unique_years = unique_years.sort(function(a, b) {
      return a - b;
    })
    console.log(unique_years)
    var trace1 = {
      x: unique_years,
      y: HP,
      type: "scatter",
      name: "PS"
  
    };
    var layout = { title: "Average Metric Horsepower of " + car_brand +  " Models" ,
    titlefont: {
      size: 36
    },
    yaxis: {title: "Average HP of all Models"},
    };

    data = [trace1]
    Plotly.newPlot("plot", data, layout)
}



//Event Listener functions

update =  function(){Generate_HP_Graph(document.getElementById("brand").value)}



document.getElementById("brand").addEventListener("change", update);