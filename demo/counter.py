from nmigen import *

class Counter(Elaboratable):
    def __init__(self, limit):
        self.val = Signal(range(limit))
    
    def elaborate(self, platform):
        m = Module()

        m.d.sync += self.val.eq(self.val + 1)

        return m