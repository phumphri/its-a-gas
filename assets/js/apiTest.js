window.onload = () => {
  let queryUrl = "https://its-a-gas.herokuapp.com/models_offered_by_year";
  axios.get(queryUrl)
       .then( response => {
         console.log(response);
       })
       .catch( err => {
         console.log(err);
       })
}
