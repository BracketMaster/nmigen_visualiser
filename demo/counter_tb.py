from counter import Counter
from nmigen.back.pysim import Simulator, Tick, Settle
from nmigen import Module

from nmigen_visualiser.vis_interface import VisInterface
from frontend.frontend import html, js

def get_state():
    # the only thing your get_state function
    # is allowed to yield are nMigen signals
    # That is, statements such as ``yield Tick()``
    # ``yield Settle()`` or simply ``yield``

    #This function should return a string.
    return str((yield dut.val))


def process():
    for tick in range(4):
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
    period = period,
    html = html,
    js = js,
    get_state=get_state,
    # makes the current file title the browser tab title
    title = __file__[:-3]
    )

visual_sim.run(process)