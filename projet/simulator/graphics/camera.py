from ..utils.vector import Vector, Vector2


class Camera:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.position = Vector2(0, 0)
        self.scale = 1

    def to_screen_coords(self, position):
        """ Converts the world-coordinate position to a screen-coordinate. """

        return (position - self.position) * self.scale + 0.5 * self.screen_size

    def from_screen_coords(self, position):
        """ Converts the screen-coordinate position to a world-coordinate. """
        return (position - 0.5*self.screen_size)/self.scale + self.position
