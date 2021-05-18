from ..utils.vector import Vector, Vector2
from .constants import G


def gravitational_force(pos1, mass1, pos2, mass2):
    """ Return the force applied to a body in pos1 with mass1
        by a body in pos2 with mass2
    """
    dif = pos2-pos1
    return dif*G*mass1*mass2/Vector.norm(dif)**3


class IEngine:
    def __init__(self, world):
        self.world = world

    def derivatives(self, t0, y0, h = 0.01):
        """ This is the method that will be fed to the solver
            it does not use its first argument t0,
            its second argument y0 is a vector containing the positions
            and velocities of the bodies, it is laid out as follow
                [x1, y1, x2, y2, ..., xn, yn, vx1, vy1, vx2, vy2, ..., vxn, vyn]
            where xi, yi are the positions and vxi, vyi are the velocities.

            Return the derivative of the state, it is laid out as follow
                [vx1, vy1, vx2, vy2, ..., vxn, vyn, ax1, ay1, ax2, ay2, ..., axn, ayn]
            where vxi, vyi are the velocities and axi, ayi are the accelerations.
        """
        #méthode naïve où on calcule les intéractions entre toutes les planètes pour avoir les ai puis on intègre pour avoir les vi
        n = len(self.world)
        res = Vector(4*n)
        for i in range(n):

            body_i = self.world.get(i)
            m_i = body_i.mass
            pos_i = body_i.position
            #calcul de la force
            f=Vector(2)
            for j in range(n):
                if(i!=j):
                    body_j = self.world.get(j)
                    m_j = body_j.mass
                    pos_j = body_j.position
                    f+=gravitational_force(pos_i,m_i,pos_j,m_j)

            #calcul des accélérations et nouvelles vitesses, mises dans le tableau
            a_i = f /m_i
            vx_i = y0[2*i] + h * a_i[0]
            vy_i = y0[2*i+1] + h * a_i[1]
            res[2*i] = vx_i
            res[2*i+1] = vy_i
            res[2*n+2*i] = a_i[0]
            res[2*n+2*i+1] = a_i[1]
        print("%s\n", res)
        return res




    def make_solver_state(self):
        """ Returns the state given to the solver, it is the vector y in
                y' = f(t, y)
            In our case, it is the vector containing the
            positions and speeds of all our bodies:
                [x1, y1, x2, y2, ..., xn, yn, vx1, vy1, vx2, vy2, ..., vxn, vyn]
            where xi, yi are the positions and vxi, vyi are the velocities.
        """
        bodies = self.world.bodies()
        y0 = []
        v0=[]
        for body in bodies:
            y0.append(body.position[0])
            y0.append(body.position[1])
            v0.append(body.velocity[0])
            v0.append(body.velocity[1])

        y0.extend(v0)
        n= len(y0)
        y1 =Vector(n)
        for i in range(n):
            y1[i]=y0[i]
        return y1


class DummyEngine(IEngine):
    pass
