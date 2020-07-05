from counter import Counter
from nmigen.back.pysim import Simulator
from nmigen import Module

from nmigen_visualiser.vis_interface import VisInterface
from frontend.frontend import html, js

def get_state():
    print("Getting State")
    print((yield dut.val))
    print((yield dut.val))
    print((yield dut.val))
    return {6:6}


def process():
    for tick in range(3):
        print((yield dut.val))
    return {6:6}

# setup nMigen simulation
dut = Counter(limit=20)
m = Module()
m.submodules.dut = dut
sim = Simulator(m)
period = 1e-6
sim.add_clock(period)

val = None

def wrapper():
    proc = process()
    ret = next(proc)
    while True:
        try:
            ret = proc.send((yield ret))
        except StopIteration as e:
            global val
            val = e
            return

# setup visual frontend
visual_sim = VisInterface(
    sim = sim,
    period = period,
    html = html,
    js = js,
    get_state=get_state,
    # makes the current file title the browser tab title
    title = __file__[:-3]
    )
visual_sim.run(3)