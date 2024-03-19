/*!

=========================================================
* Argon Dashboard Tailwind - v1.0.1
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard-tailwind
* Copyright 2022 Creative Tim (https://www.creative-tim.com)

* Coded by www.creative-tim.com

=========================================================

* This code has been modified to work with Django static files

*/

loadStylesheet("static/css/perfect-scrollbar.css");
loadJS("static/js/perfect-scrollbar.js", true);

if (document.querySelector("[slider]")) {
  loadJS("static/js/carousel.js", true);
}

if (document.querySelector("nav [navbar-trigger]")) {
  loadJS("static/js/navbar-collapse.js", true);
}

if (document.querySelector("[data-target='tooltip']")) {
  loadJS("static/js/tooltips.js", true);
  loadStylesheet("static/css/tooltips.css");
}

if (document.querySelector("[nav-pills]")) {
  loadJS("static/js/nav-pills.js", true);
}

if (document.querySelector("[dropdown-trigger]")) {
  loadJS("static/js/dropdown.js", true);

}

if (document.querySelector("[fixed-plugin]")) {
  loadJS("static/js/fixed-plugin.js", true);
}

if (document.querySelector("[navbar-main]") || document.querySelector("[navbar-profile]")) {
  if(document.querySelector("[navbar-main]")){
    loadJS("static/js/navbar-sticky.js", true);
  }
  if (document.querySelector("aside")) {
    loadJS("static/js/sidenav-burger.js", true);
  }
}

if (document.querySelector("canvas")) {
  loadJS("static/js/charts.js", true);
}

if (document.querySelector(".github-button")) {
  loadJS("https://buttons.github.io/buttons.js", true);
}

function loadJS(FILE_URL, async) {
  let dynamicScript = document.createElement("script");

  dynamicScript.setAttribute("src", FILE_URL);
  dynamicScript.setAttribute("type", "text/javascript");
  dynamicScript.setAttribute("async", async);

  document.head.appendChild(dynamicScript);
}

function loadStylesheet(FILE_URL) {
  let dynamicStylesheet = document.createElement("link");

  dynamicStylesheet.setAttribute("href", FILE_URL);
  dynamicStylesheet.setAttribute("type", "text/css");
  dynamicStylesheet.setAttribute("rel", "stylesheet");

  document.head.appendChild(dynamicStylesheet);
}
