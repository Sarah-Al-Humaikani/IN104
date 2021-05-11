from ..utils.vector import Vector, Vector2
from numpy import arange
class SolverError(Exception):
    pass


class ISolver:

    # NOTE: our systems do not depend on time,
    # so the input t0 will never be used by the
    # the derivatives function f
    # However, removing it will not simplify
    # our functions so we might as well keep it
    # and build a more general library that
    # we will be able to reuse some day

    def __init__(self, f, t0, y0, max_step_size=0.01):
        """y0 est la valeur initiale, f la fonction qui donne la dérivée"""
        self.f = f
        self.t0 = t0
        self.y0 = y0
        self.max_step_size = max_step_size

    def integrate(self, t, step_size = self.max_step_size):
        """ Compute the solution of the system at t
            The input `t` given to this method should be increasing
            throughout the execution of the program.
            Return the new state at time t.
        """
       res = self.y0
        for i in arange(self.t0,step_size,t):
            res += self.f(i,res) * step_size
            time = i

        if t - time >0:
            res += self.f(time,res)*(t-time)
        return res


class DummySolver(ISolver):


    pass
