function tick(ev) {
    ev.preventDefault();
    fetch("/tick", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
    })
  }

  function repaint(){
    const payload = fetch("/update", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({op:"read_updates"})
    })
    .then((response) => {return response.json()})
    .then((payload) => {
      // update page elements
      var ticks = document.getElementById('ticks');
      ticks.innerText = payload.ticks;
      var result = document.getElementById('result');
      result.innerText = payload.state;
    })

  }

  var form = document.getElementById('calc');
  form.addEventListener('submit', tick);
  setInterval(repaint, 50);