function do_update(payload){
  // update page elements
  var result = document.getElementById('result');
  result.innerText = payload.state;
}

var num_clicks = 0;

function clicked(){
  num_clicks += 1
  var clicks = document.getElementById('clicks')
  clicks.innerText = num_clicks
}
