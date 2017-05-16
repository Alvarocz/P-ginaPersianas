$(document).foundation()

var imgContainer = document.querySelector("#galeria");
var images = imgContainer.getElementsByTagName('img');

setTimeout(function()
{
    for (var i=0; i < images.length; i++) {
      images[i].style.opacity = "1";
    }
},250);
