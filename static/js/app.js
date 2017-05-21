$(document).foundation()

$.getJSON('/imagenes', {}, function(data) {
  var items = [];
  var container = $(".gallery-container").eq(0);

  for (var image in data) {
    var img_thumbnail = $('<div class="image-thumbnail">');
    var img = $('<img src="'+data[image].fields.url+'">');
    img_thumbnail.append(img);
    img_thumbnail.append($('<div class="image-caption">'+data[image].fields.nombre+'</div>'));
    items.push(img_thumbnail);
  }
  if (items.length == 1) {
    var new_col = $('<div class="col">');
    new_col.append(items[0]);
    container.append(new_col);
  } else if (items.length == 2) {
    for (var i=0; i < 2; i++) {
      var new_col = $('<div class="col">');
      new_col.append(items[i]);
      container.append(new_col);
    }
  } else {
    var mult = 0;
    if (items.length % 3 == 0) { mult = 3; }
    else if (items.length % 5 == 0) { mult = 5; }
    else if (items.length % 2 == 0) { mult = 4; }
    else { mult = 1; }
    var new_col = $('<div class="col">');
    for (var i=1; i <= items.length; i++) {
      new_col.append(items[i-1]);
      if (i % mult == 0) {
        container.append(new_col);
        new_col = $('<div class="col">');
      }
    }
  }
});

var img_container = document.querySelector("#galeria");
var images = img_container.getElementsByTagName('img');
setTimeout(function() {
  for (var i=0; i < images.length; i++) {
    images[i].style.opacity = "1";
  }
},250);
