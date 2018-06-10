let axios = require('axios');

let make = 'ford',
    model = 'mustang',
    baseQueryUrl = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims';

// request based on parameters above
axios.get(`${baseQueryUrl}&make=${make}&model=${model}`)
     .then( (response) => {
        console.log(response);
     });
