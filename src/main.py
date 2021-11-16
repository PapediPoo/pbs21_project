import taichi as ti
import open3d as o3d
import numpy as np
from SimulationObjects.ParticleObject import ParticleObject
from SimulationObjects.Racket import Racket
from SimulationObjects.Wall import Wall
from Utils.Timing import delta_time


ti.init(arch=ti.cuda)   # IMPORTANT NOTE: if you dont have an Nvidia GPU or no GPU alltogether, set this accordingly to ti.gpu ro ti.cpu. Expect lesser performance though


# Singleton class that handles the overall game state
class Game(object):
    def __init__(self) -> None:
        self.gui = ti.GUI("Game", res=512, fast_gui=False)
        self.simulation_objects = []

        # Add all scene objects to the list of simulation objects
        self.simulation_objects.append(ParticleObject())                                        # creates a swarm of particles in the scene (just as an example)
        self.simulation_objects.append(Racket(ti.Vector([0.5, 0.05]), ti.Vector([0.3, 0.05])))  # creates the racket that is controlled by the player
        self.simulation_objects.append(Wall(ti.Vector([0, 0]), ti.Vector([0.1, 1])))            # creates a wall at the left border of the screen
        self.simulation_objects.append(Wall(ti.Vector([0.9, 0]), ti.Vector([1, 1])))

        self.dt = 0
    
    # processes the input on each object of the simulation
    def update_input(self):
        self.gui.get_event()    # polls the input events

        for obj in self.simulation_objects:
            obj.process_input(self.gui)

    # processes the simulation aspect of each object
    def update_physics(self):
        for b in self.simulation_objects:
            b.step()
    
    # renders the objects in the scene
    def update_visuals(self):
        for obj in self.simulation_objects:
            obj.display(self.gui)
        
        self.gui.show()
    
    # runs a single update loop of the game. returns true if the game is still running
    def update(self):
        self.dt = delta_time()

        self.update_input()
        self.update_physics()
        self.update_visuals()

        return self.gui.running


def main():
    game = Game()

    while game.update():
        pass

if __name__ == "__main__":
    main()