let axios = require('axios');
let fs = require('fs');

// Defining generating object
carData = {
  modelData: [],
  itemsProcessed: 0
}

// Temporary, key string is search parameter, change this key to generate make file name
let key = 'Kia'
let baseQueryUrl = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims';

// Using axios to hit API with a get request
// TODO: make for loop to run trim request for years
axios.get(`${baseQueryUrl}&make=${key}`, {
  responseType: 'json',
  transformResponse: [data => {
    return JSON.parse(data.slice(2, data.length - 2))
  }]
}).then(response => {
  // Data received Pushing it to object
  response.data.Trims.forEach( (entry, index, array) => {
    carData.modelData.push(entry);
    carData.itemsProcessed++;

    if (carData.itemsProcessed == array.length) {
      // console.log(carData);
      // Call toFile function to generate the CSV file
      ToFile(carData.modelData);
    }
  });
}).catch(error => {
  if (err) throw err;
})


let ToFile = obj => {
    const replacer = (key, value) => value === null ? "" : value;
    const header = Object.keys(obj[0]);

    let csv = obj.map( row => {
        return header.map( fieldName => {
            return JSON.stringify(row[fieldName], replacer)
        }).join(',')
    });
    csv.unshift(header.join(','))
    // console.log(csv.join('/r/n'));

    fs.writeFile(`${key}.csv`, csv.join('\r\n'), err => {
        if (err) throw err;
        console.log(`CSV file was successfully created: ${key}.csv`);
    })

    return 0;
}
