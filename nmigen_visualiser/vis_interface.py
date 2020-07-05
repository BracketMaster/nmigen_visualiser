import requests
from time import sleep
from nmigen_visualiser.vis_backend import start_webapp
from multiprocessing import Process, Queue

from nmigen.back.pysim import Simulator
from nmigen import Signal

class VisInterface():
    def __init__(self, sim, period, html, js, get_state, title=None):
        print("DOING INIT")
        self.sim = sim
        self.period = period
        self.queue = Queue()
        self.get_state = get_state

        # private varibles
        self.__timestamp = 0
        self.__addr = 'http://127.0.0.1:2000/'
        self.__state = None
        self.__html = html
        self.__js = js
        self.__title = title
        self.__state = None

    def run(self, process):
        print("RUNNING")

        def state_wrapper():
            proc = self.get_state()
            ret = next(proc)
            while True:
                try:
                    if type(ret) != type(Signal()):
                        raise TypeError(f"Argument to yield must be of "+
                            f"type {type(Signal())} not type {type(ret)}"+
                            "\nFunction get_state must only yield signals.")
                    ret = proc.send((yield ret))
                except StopIteration as e:
                    self.__state = e
                    return

        
        self.sim.add_process(state_wrapper)
        self.sim.run()

        print(self.__state)

        return


        #self.__sim_finished = False
        #def frontend_runner():
        #    yield from process()
        #    self.__sim_finished = True

        #self.sim.add_sync_process(frontend_runner)
        #while not self.__sim_finished:
        #    self.queue.get()
        #    self.queue.put(
        #        {"state" : self.get_state(),
        #        "ticks":self.__timestamp}
        #        )
        
        # teardown webapp
        #p.terminate()
        #print("TERMINATED")
        #p.join()

    def update_state(self, curr_state):
        global state
        state = curr_state

    def __update_requested(self):
        res =  requests.post( self.__addr + 'update', 
                json={"op":"request_status"})
        sleep(.05)
        return res.json()["status"]["step_requested"]

    def __post_state(self, ticks, state):
        res =  requests.post( self.__addr + 'update', 
                json={"op" : "write_updates",
                    "ticks" : ticks, 
                    # TODO : change counter_val to state
                    "state" : state}
                    )
    
    def __exit__(self):
        self.queue.close()
        self.queue.join_thread()