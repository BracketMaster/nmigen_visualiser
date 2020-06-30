from counter import Counter
from nmigen.back.pysim import Simulator
from nmigen import Module

from nmigen_visualiser.vis_interface import VisInterface
from frontend.frontend import html, js

def process():
    for tick in range(5):
        visual_sim.update_state((yield dut.val))
        yield

# setup nMigen simulation
dut = Counter(limit=20)
m = Module()
m.submodules.dut = dut
sim = Simulator(m)
period = 1e-6
sim.add_clock(period)

# setup visual frontend
visual_sim = VisInterface(
    sim = sim,
    process = process, 
    period = period,
    html = html,
    js = js,
    # makes the current file title the browser tab title
    title = __file__[:-3]
    )
visual_sim.run()