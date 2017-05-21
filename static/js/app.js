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
  var i = 1;
  var num_cols;
  if (items.length == 1) { num_cols = 1; }
  else if (items.length == 2) { num_cols = 2; }
  else if (items.length == 3) { num_cols = 3; }
  else if (items.length % 4 == 0) { num_cols = 4; }
  else if (items.length % 6 == 0) { num_cols = 3; }
  else { num_cols = 5; }
  var new_col = $('<div class="col">');
  for (var j=0; j < items.length; j++) {
    new_col.append(items[j]);
    if (i == items.length/num_cols) {
      container.append(new_col);
      new_col = $('<div class="col">');
      i = 0;
    }
    i ++;
  }
  if (new_col[0].childNodes.length > 0) { container.append(new_col); }
  var images = $(".gallery-container img");
  for (var i=0; i < images.length; i++) {
    images[i].addEventListener("load", function(evt) {
      evt.target.style.opacity = "1";
    });
  }
});
