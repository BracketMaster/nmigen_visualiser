import requests
from time import sleep
from nmigen_visualiser.vis_backend import start_webapp
from multiprocessing import Process, Queue

from nmigen.back.pysim import Simulator, Settle, Tick
from nmigen import Signal

from time import sleep

class VisInterface():
    def __init__(self, sim, period, html, js, get_state, title=None):
        self.sim = sim
        self.period = period
        self.get_state = get_state

        # private varibles
        self.__addr = 'http://127.0.0.1:2000/'
        self.__state = None
        self.__html = html
        self.__js = js
        self.__title = title
        self.__state = None

    def run_sync(self, process):

        def state_wrapper():
            proc = self.get_state()

            # start self.get_state() as function generator
            ret = next(proc)
            while True:
                try:
                    # the get_state function is only allowed to 
                    # yield signals
                    if type(ret) != type(Signal()):
                        raise TypeError(f"Argument to yield must be of "+
                            f"type {type(Signal())} not type {type(ret)}"+
                            "\nFunction get_state must only yield signals.")
                    ret = proc.send((yield ret))
                
                # e contains the return value from 
                # self.get_state()
                except StopIteration as e:
                    return e

        # use queue to communicate bewtween this process
        # and webapp process

        self.queue = Queue()
        # start webapp as separate process
        p = Process(target=start_webapp, args=(
            self.__addr,
            self.__title,
            self.__html,
            self.__js,
            self.queue
                )
            )
        p.start()

        def process_wrapper():

            # we can implement callbacks by blocking on queue
            # recieves
            self.queue.get()
            state = yield from state_wrapper()
            self.queue.put({"state" : state.value})

            proc = process()
            # must get first element out of generator
            # before we can use proc.send()
            ret = next(proc)

            while True:
                try:
                    # keep advancing until we hit another Tick() 
                    # statement
                    while type(ret) not in (type(None), type(Tick)):
                        ret = proc.send((yield ret))

                    # block until we get tick() post request from 
                    # javascript
                    self.queue.get()
                    ret = proc.send((yield ret))
                    state = yield from state_wrapper()
                    self.queue.put({"state" : state.value})

                except StopIteration:
                    state = yield from state_wrapper()
                    self.queue.put({"state" : state.value})
                    sleep(.6)
                    break



        self.sim.add_sync_process(process_wrapper)
        self.sim.run()
        
        # teardown webapp
        p.terminate()
        p.join()
    
    def __exit__(self):
        self.queue.close()
        self.queue.join_thread()