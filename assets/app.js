let axios = require('axios');

let make = 'ford',
    model = 'mustang',
    baseQueryUrl = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims';

// request based on parameters above
axios.get(`${baseQueryUrl}&make=${make}&model=${model}`, {
  responseType: 'json',
  transformResponse: [(data) => {
    return JSON.parse(data.slice(2, data.length-2));
  }]
})
     .then( response => {
        let data = response.data;
        console.log(data);
     })
     .catch( error => {
       console.log(error);
     });
