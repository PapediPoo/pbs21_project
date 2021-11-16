import taichi as ti
import open3d as o3d
import numpy as np
from SimulationObjects.SimulationObject import SimulationObject

# This is an example simulation object that represents a collection of particles that are attracted to each other based on their distance
# This is ported over from an example project from the class to show how the in-class examples fit into our project
@ti.data_oriented
class ParticleObject(SimulationObject):
    def __init__(self, N=50, dt=1./60, substeps=50):
        self.N = N
        self.dt = dt
        self.substeps = 50
        self.paused = False

        self.x = ti.Vector.field(
            2, float, self.N, needs_grad=True
        )  # particle positions
        self.v = ti.Vector.field(2, float, self.N)  # particle velocities
        self.U = ti.field(float, (), needs_grad=True)  # potential energy

        self.init()

    @ti.kernel
    def init(self):
        for i in self.x:
            self.x[i] = [ti.random(), ti.random()]
            self.v[i] = [0, 0]
        self.U[None] = 0

    @ti.kernel
    def compute_U(self):
        for i, j in ti.ndrange(self.N, self.N):
            r = self.x[i] - self.x[j]
            # r.norm(1e-3) is equivalent to ti.sqrt(r.norm()**2 + 1e-3)
            # This is to prevent 1/0 error which can cause wrong derivative
            self.U[None] += -1 / r.norm(1e-3)  # U += -1 / |r|

    @ti.kernel
    def advance(self):
        for i in self.x:
            self.v[i] += self.dt / 1000 * -self.x.grad[i]  # dv/dt = -dU/dx
            self.x[i] += self.dt / 1000 * self.v[i]  # dx/dt = v

    def step(self):
        if self.paused:
            return
        for _ in range(self.substeps):
            with ti.Tape(self.U):
                # Kernel invocations in this scope contribute to partial derivatives of
                # U with respect to input variables such as x.
                self.compute_U()  # The tape will automatically compute dU/dx and save the results in x.grad
            self.advance()
    
    def display(self, gui):
        gui.circles(self.x.to_numpy())
    
    def process_input(self, gui):
        pass

