window.onload = () => {
  console.log("System Success");



  //Event Listener for home
  document.getElementById('home-tab').addEventListener("click", e => {
    // Do something perhaps an animation?
    console.log("home tab");
  });

  //Event Listener for second tab
  document.getElementById('analysis1').addEventListener("click", e => {
    console.log("Analysis 1 tab");
  });

  // Event Listener for third tab
  document.getElementById('contact-tab').addEventListener('click', e => {
    console.log("contact tab");
  })

}
