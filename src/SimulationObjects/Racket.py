import taichi as ti
from SimulationObjects.SimulationObject import SimulationObject

class Racket(SimulationObject):

    def __init__(self, init_position : ti.Vector, size : ti.Vector, dt=1/60):
        self.position = init_position
        self.velocity = ti.Vector([0,0])
        self.size = size
        self.mass = 0
        self.dt = dt

    def step(self):
        # this is where the physics solver will be implemented
        self.position = self.position + self.dt * self.velocity
        # TODO: Collision check with other objects (e.g. Walls) and set the velocity accordingly
    
    # Renders the racket as a rectangle
    def display(self, gui):
        half_extents = self.size / 2
        gui.rect(self.position - half_extents, self.position + half_extents, color=0xffffff)
    
    # processes the player input and sets the racked speed on the x axis accordingly
    def process_input(self, gui):
        if gui.is_pressed(ti.GUI.LEFT):
            self.velocity = ti.Vector([-1, 0])
        elif gui.is_pressed(ti.GUI.RIGHT):
            self.velocity = ti.Vector([1, 0])
        else:
            self.velocity = ti.Vector([0, 0])