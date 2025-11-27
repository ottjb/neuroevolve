import random as r
from constants import WIDTH, HEIGHT

class Blob():
    def __init__(self):
        self.pos = (r.randrange(0, WIDTH), r.randrange(0, HEIGHT))
        self.facing = r.randrange(0, 8)

    def clamp_position(self):
        self.pos = list(self.pos)
        self.pos[0] = max(min(WIDTH - 1, self.pos[0]), 0)
        self.pos[1] = max(min(HEIGHT - 1, self.pos[1]), 0)
        self.pos = tuple(self.pos)