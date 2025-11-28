import random as r
from constants import WIDTH, HEIGHT
from Utility import get_random_color

class Blob():
    def __init__(self, parent1=None, parent2=None):
        self.pos = (r.randrange(0, WIDTH), r.randrange(0, HEIGHT))
        self.facing = r.randrange(0, 8)
        if parent1 and parent2:
            pass
        else:
            self.color = get_random_color()

    def clamp_position(self):
        self.pos = list(self.pos)
        self.pos[0] = max(min(WIDTH - 1, self.pos[0]), 0)
        self.pos[1] = max(min(HEIGHT - 1, self.pos[1]), 0)
        self.pos = tuple(self.pos)

    def wrap_position(self):
        self.pos = list(self.pos)
        self.pos[0] = self.pos[0] % WIDTH
        self.pos[1] = self.pos[1] % HEIGHT
        self.pos = tuple(self.pos)