import random as r
from Brain import Brain
from constants import WIDTH, HEIGHT, ENERGY_ON_CONSUMPTION, MAX_ENERGY, REPRODUCTION_COOLDOWN, REPRODUCTION_ENERGY_MIN
from Utility import get_random_color, blend_colors
from typing import Tuple, Optional, Set

class Blob():
    def __init__(self, pos: Tuple[int, int], parent1: Optional['Blob'] = None, parent2: Optional['Blob'] = None):
        self.max_energy = 200
        self.alive = True
        self.pos = pos
        self.facing = r.randrange(0, 8)
        self.reproduction_cooldown = REPRODUCTION_COOLDOWN
        if parent1 and parent2:
            self.brain = Brain()
            self.energy = int(parent1.energy / 2 + parent2.energy / 2)
            self.color = [255, 255, 255]
            #self.color = blend_colors(parent1.color, parent2.color)
        else:
            self.brain = Brain()
            self.energy = 200
            self.color = get_random_color()

    def can_reproduce(self) -> bool:
        if self.energy >= REPRODUCTION_ENERGY_MIN and self.reproduction_cooldown <= 0:
            return True
        return False
    
    def check_adjacent(self, blob_positions: Set[Tuple[int, int]: Optional['Blob']]) -> Optional['Blob']:
        x, y = self.pos

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                adjacent_pos = ((x + dx) % WIDTH, (y + dy) % HEIGHT)
                if adjacent_pos in blob_positions:
                    potential_mate = blob_positions[adjacent_pos]

                    if potential_mate != self and potential_mate.can_reproduce():
                        return potential_mate
        return None

    def wrap_position(self) -> None:
        x, y = self.pos
        self.pos = (x % WIDTH, y % HEIGHT)

    def set_dead(self) -> None:
        self.alive = False

    def get_next_move(self) -> int:
        return self.brain.next_move()
    
    def eat_food(self) -> None:
        self.energy = min(self.energy + ENERGY_ON_CONSUMPTION, MAX_ENERGY)