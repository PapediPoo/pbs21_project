import taichi as ti
import numpy as np

# This is the superclass of objects that should be simulated in the scene
@ti.data_oriented
class SimulationObject():
    def __init__(self) -> None:
        pass

    # Note: the execution order of the following three methods goes as follows: process_input -> step -> display.
    # The advantage of processing the input before the step is that the player input can be directly processed in the same frame, effectively reducing input latency. 
    # The same goes for rendering directly after the simulation update step.

     # This method is called for each physics step
    def step(self):
        pass
     # This method is called when the object is rendered
    def display(self, gui):
        pass

    # this method is called on each frame and is intended for input processing 
    def process_input(self, gui):
        pass
