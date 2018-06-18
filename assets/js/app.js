let axios = require('axios');
let fs = require('fs');

// Defining generating object
carData = {
  modelData: [],
}

// Temporary, key string is search parameter, change this key to generate make file name
// IMPORTANT: CHANGE THE KEY AND YEARS PARAMETER ONLY
let key = 'Maserati',
    baseQueryUrl = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims',
    years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
    dataGather
// Using axios to hit API with a get request
// TODO: make for loop to run trim request for years
dataGather = years.map(year => {
  return (axios.get(`${baseQueryUrl}&make=${key}&year=${year}`, {
    responseType: 'json',
    transformResponse: [data => {
      return JSON.parse(data.slice(2, data.length - 2))
    }]
  }));

})

Promise.all(dataGather)
       .then( response => {
         response.forEach( (res, index, array) => {
           res.data.Trims.forEach( res => {
             // console.log(res);
             carData.modelData.push(res);
           })
           // console.log(res.data.Trims[0])
         })
         // console.log(carData.modelData);
         ToFile(carData.modelData);
       })
       .catch( err => {
         if (err) throw err;
       })


// =========================================================================================================
// Function definition for file writing

let ToFile = obj => {
  const replacer = (key, value) => value === null ? "" : value;
  const header = Object.keys(obj[0]);

  let csv = obj.map(row => {
    return header.map(fieldName => {
      return JSON.stringify(row[fieldName], replacer)
    }).join(',')
  })
  csv.unshift(header.join(','))
  // console.log(csv.join('/r/n'));

  fs.writeFile(`${key}.csv`, csv.join('\r\n'), err => {
    if (err) throw err;
    console.log(`CSV file was successfully created: ${key}.csv`);
  })

  return 0;
}
