  function do_update(payload){
      // update page elements
      var ticks = document.getElementById('ticks');
      ticks.innerText = payload.ticks;
      var result = document.getElementById('result');
      result.innerText = payload.state;
  }