# nMigen Simulator Visualiser

![](docs/visualiser_session.png)

[What is nMigen?](#what-is-nmigen)

Sometimes you have very complicated RTL that is
an implementation of a regular structure such as
a tree or a butterfly DSP chain.

Debugging might be much easier if you could simply
draw your butterfly DSP chain with values in boxes
instead of browsing waveforms or using print statements.

Behold! The nMigen Visualiser. It utilises a flask
server which calls into the nmigen simulator.
You can put a javascript frontend using ``d3.js``
or perhaps ``vis.js``that can grab the values from
flask and render a drawing for you.

An added bonus, a visualising simulator may 
also serve as a good form of documentation
in the future.

# Running Demo

This code here is primarily meant to serve as a starting 
point for other projects.

An nMigen counter is instantiated and its value is drawn
on a webpage. Clicking ``Step Sim`` advances the simulation.

## Steps

You may want to do the following steps in 
a python virtual environment.

```bash
git clone https://github.com/BracketMaster/nmigen-visualiser
cd nmigen-visualiser
python setup.py develop
python demo/counter_tb.py
```

You should now be able to run the demo 
in the intro picture of this README.

# Extending and Re-using
You will first need to install ``nmigen_visualiser``
on your system like so:

Go ahead and look at the ``counter_tb.py`` demo in 
the ``./demo`` directory.


# What is [nMigen](https://github.com/nmigen/nmigen)?
nMigen is an RTL implemented as a Python DSL.

It has the following strengths:

 - Emits Yoysys RTLIL
 - Emits veilog through Yosys RTLIL
 - Clean interface to FOSS SymbiYosys formal verification suite.
 - Clean and natural idioms.
 - Built in Python RTL Simulator
 - Will soon be capable of using the speedy YosysCXX simulator backend
 - Allows for anything Python enabling sane management of large codebases
   - Unit tests
   - list comprehensions
   - the list goes on...
 - nMigen SOC comes with nice tools such as Wishbone.

# TODO
 - [ ] break HTML script into separate ``js`` file
 - [ ] move counter_tb into demo folder
 - [ ] modularize with setup.py
 - [ ] instructions for modifying for your needs
 - [ ] replace CSS with actual files