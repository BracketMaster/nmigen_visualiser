import requests
from time import sleep
from visualiser.vis_backend import start_webapp
from multiprocessing import Process

class VisInterface():
    def __init__(self, sim, process, period):
        self.sim = sim
        self.process = process
        self.period = period

        # private varibles
        self.__addr = 'http://127.0.0.1:2000/'
        self.__state = None
        self.__sim_finished = False

    def run(self):
        # start webapp as backgroung process
        p = Process(target=start_webapp, args=(self.__addr,))
        p.start()

        timestamp = 0
        def frontend_runner():
            yield from self.process()
            self.__sim_finished = True

        self.sim.add_sync_process(frontend_runner)
        while not self.__sim_finished:
            if self.__update_requested():
                self.sim.run_until(timestamp + self.period)
                timestamp += self.period
                self.__post_state(timestamp, state)
        
        # teardown webapp
        p.terminate()
        p.join()

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