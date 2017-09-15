$(document).foundation()

$.getJSON('/getimages', {}, function(data) {
  var items = [];
  var columns = [];
  var container = $(".gallery-container").eq(0);

  for (var image in data) {
    var img_thumbnail = $('<div class="image-thumbnail">');
    var img = $('<img src="'+data[image].fields.url+'">');
    img_thumbnail.append(img);
    img_thumbnail.append($('<div class="image-caption">'+data[image].fields.nombre+'</div>'));
    items.push(img_thumbnail);
  }
  var num_cols;
  if (items.length == 1) { num_cols = 1; }
  else if (items.length == 2) { num_cols = 2; }
  else if (items.length == 3) { num_cols = 3; }
  else if (items.length % 4 == 0) { num_cols = 4; }
  else if (items.length % 6 == 0) { num_cols = 3; }
  else { num_cols = 5; }
  var new_col = $('<div class="col">');
  
  // Create the column nodes
  console.log(num_cols);
  for (var c=0; c < num_cols; c++) {
    new_col = $('<div class="col">');
    columns.push(new_col);
  }
  
  // Push the image thumbnails to each column by rows
  var i = 0;
  for (var j=0; j < items.length; j++) {
    if (i == num_cols) {
      i = 0;
    }
    columns[i].append(items[j]);
    i ++;
  }
  for (var c=0; c < num_cols; c++) {
    container.append(columns[c]);
  }
  
  var images = $(".gallery-container img");
  for (var i=0; i < images.length; i++) {
    images[i].addEventListener("load", function(evt) {
      evt.target.style.opacity = "1";
    });
  }
});
