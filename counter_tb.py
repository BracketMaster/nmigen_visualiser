from counter import Counter
from nmigen.back.pysim import Simulator
from nmigen import Module
from visualiser.vis_interface import VisInterface

def print_sig(sig, format=None):
    if format == None:
        print(f"{sig.__repr__()} = {(yield sig)}")
    if format == "h":
        print(f"{sig.__repr__()} = {hex((yield sig))}")

def process():
    for tick in range(5):
        visual_sim.update_state((yield dut.val))
        yield

dut = Counter(limit=20)
m = Module()
m.submodules.dut = dut
sim = Simulator(m)

period = 1e-6
sim.add_clock(period)
visual_sim = VisInterface(sim, process, period)
visual_sim.run()