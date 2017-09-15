$(document).foundation()

$.getJSON('/getvideos', {}, function(data) {
  var items = [];
  var columns = [];
  var container = $("section#videos");

  for (var video in data) {
    var video_thumb = $('<div class="fb-video" data-href="'+data[video].fields.url+'" data-width="600" data-show-text="false">');
    video_thumb.append('<div class="fb-xfbml-parse-ignore">'+
                       '<blockquote cite="'+data[video].fields.url+'"></blockquote></div>');
    items.push(video_thumb);
  }
  console.log(items);
  var i = 0;
  var new_row = $('<div class="row">');
  for (var j=0; j<items.length; j++) {
    var col = $('<div class="small-12 medium-4 columns">');
    col.append(items[j]);
    new_row.append(col);
    if (i == 2) {
      container.append(new_row);
      new_row = $('<div class="row">');
      i = 0;
    }
    console.log(new_row);
    if (new_row.length > 0) { container.append(new_row); }
    i ++;
  }
});
