"""
This file implements the flask server.
The nmigen simulator can write to the state variable.
The javascript frontend can read the state variable.
"""
import webbrowser
from threading import Timer

from flask import jsonify
from flask import render_template
from flask import request, jsonify
from flask.cli import main

from flask import Flask
app = Flask(__name__)

# TODO : convert this file into a class avoiding global variables

addr = None
title = None
html = None
js = None
state = False
step_requested = False
ticks = 0
queue = None

def open_browser():
      webbrowser.open_new(addr)


@app.route("/")
def index():
    return render_template(
        "base.html",
        title=title,
        html=html,
        js=js)

@app.route("/update", methods=["POST"])
def update():

    global step_requested
    global state
    global ticks

    payload = request.json
    # the python nmigen simulation can check if update is requested
    # the python nmigen simulation can write its updates
    # the javascipt visualisation can read in the current nmigen state
    if "op" in payload:

        if payload["op"] == "request_status":
            return jsonify({"status": 
                           {"step_requested": step_requested}
                           })

        if payload["op"] == "write_updates":
            step_requested = False
            state = payload["state"]
            ticks = payload["ticks"]

        if payload["op"] == "read_updates":
            return jsonify(
                {"state" : state,
                "ticks":ticks}
                )

    return jsonify({"return": None})

@app.route("/tick", methods=["POST"])
def tick():
    global step_requested
    step_requested = True
    queue.put(None)
    recv = queue.get()
    return jsonify(recv)

def start_webapp(_addr, _title, _html, _js, _queue):
    # in general, shouldn't use global
    # variables
    global addr
    addr = _addr
    global title
    title = _title
    global html
    html = _html
    global js
    js = _js
    global queue
    queue = _queue

    # only log errrors
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    # open browser and start app
    Timer(1, open_browser).start();
    app.run(port=2000)