import os

# get html and js as text
html = open(os.path.dirname(os.path.realpath(__file__))+'/frontend.html',"r").read()
js = open(os.path.dirname(os.path.realpath(__file__))+'/frontend.js',"r").read()