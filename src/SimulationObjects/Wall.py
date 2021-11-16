import taichi as ti
from SimulationObjects.SimulationObject import SimulationObject

# Renders a wall given two corner positions
class Wall(SimulationObject):
    def __init__(self, bottom_left_corner : ti.Vector, top_right_corner : ti.Vector):
        self.bl_corner = bottom_left_corner
        self.tr_corner = top_right_corner
        self.mass = 0

    def step(self):
        # this is where the physics solver will be implemented
        pass

    def display(self, gui):
        gui.rect(self.bl_corner, self.tr_corner, color=0xffffff)

    def process_input(self, gui):
        pass