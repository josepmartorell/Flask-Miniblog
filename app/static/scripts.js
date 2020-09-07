// scripts.js

   /* read more
    * -------------------------------------------------- */

  function myFunction() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("myBtn");

    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }

   /* search engine
    * -------------------------------------------------- */

  function myFunction2() {
    var intro_value = document.getElementById("mySearch");
    alert('Value selected: ' + intro_value.value + ".\n\nPress OK to send query...")
  }