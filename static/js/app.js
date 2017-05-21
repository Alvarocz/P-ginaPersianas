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
    var i = 1;
    var num_cols;
    if (items.length % 4 == 0) { num_cols = 2; }
    else if (items.length % 6 == 0) { num_cols = 3; }
    else if (items.length % 10 == 0) { num_cols = 5; }
    else { num_cols = items.length; }
    console.log(num_cols, items.length);
    var new_col = $('<div class="col">');
    for (var j=0; j < items.length; j++) {
      new_col.append(items[j]);
      if (i == num_cols) {
        container.append(new_col);
        new_col = $('<div class="col">');
        i = 0;
      }
      i ++;
    }
    console.log(new_col);
  }
  var images = $(".gallery-container img");
  for (var i=0; i < images.length; i++) {
    images[i].addEventListener("load", function(evt) {
      evt.target.style.opacity = "1";
    });
  }
});
