  function do_update(payload){
      // update page elements
      var ticks = document.getElementById('ticks');
      ticks.innerText = payload.ticks + " (s)";
      var result = document.getElementById('result');
      result.innerText = payload.state;
  }

  var num_clicks = 0;

  function click(ev){
    ev.preventDefault();
    num_clicks += 1
    var clicks = document.getElementById('clicks')
    clicks.innerText = num_clicks
  }

  var click_me = document.getElementById('click_me');
  click_me.addEventListener('submit', click);