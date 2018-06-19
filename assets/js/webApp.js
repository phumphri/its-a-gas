window.onload = () => {
  console.log("System Success");
  let dataArea = document.getElementById('overlaySection');

  //Event Listener for home
  document.getElementById('home-tab').addEventListener("click", e => {
    // Do something perhaps an animation?
    console.log("home tab");
  });

  //Event Listener for second tab
  document.getElementById('analysis1').addEventListener("click", e => {
    // let sSection = document.getElementById('overlaySectionSecondTab');
    // if (!sSection.classList.contains('overlayclick')) {
    //   sSection.classList.remove('overlayclick');
    //   sSection.classList.add('overlayclick');
    // }
  });

  // Event Listener for third tab
  document.getElementById('contact').addEventListener('click', e => {
    // let tSection = document.getElementById('overlaySectionThirdTab');
    // if (tSection.classList.contains('overlayclick')) {
    //   tSection.classList.remove('overlayclick');
    //   tSection.classList.add('overlayclick');
    // }
  })

}
