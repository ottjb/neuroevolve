from Blob import Blob
from Food import Food
from constants import DIR_MOVEMENTS, WIDTH, HEIGHT, ENERGY_DECAY_RATE, REPRODUCTION_COOLDOWN
from typing import List, Tuple, Optional
from Utility import get_spawn_position
import random as r

class BlobHandler():
    def __init__(self):
        self.blob_list = []
        self.foodHandler = None

    def update(self) -> List[Food]:
        occupied_positions = {b.pos for b in self.blob_list}
        new_positions = {}
        food_positions = {f.pos: f for f in self.foodHandler.get_food_list()}
        food_consumed = []

        for b in self.blob_list:
            x, y = b.pos
            move = b.brain.next_move()
            if move == 0:
                b.facing = (b.facing - 2) % 8
            elif move == 1:
                b.facing = (b.facing - 1) % 8
            elif move == 2:
                dx, dy = DIR_MOVEMENTS[b.facing]
                new_x, new_y = (x + dx, y + dy)
                new_pos = (new_x % WIDTH, new_y % HEIGHT)
                
                if new_pos not in occupied_positions:
                    new_positions[b] = new_pos
                    occupied_positions.add(new_pos)

                if new_pos in food_positions:
                    b.eat_food()
                    food_consumed.append(food_positions[new_pos])

            elif move == 3:
                b.facing = (b.facing + 1) % 8
            elif move == 4:
                b.facing = (b.facing + 2) % 8
            
            b.energy -= ENERGY_DECAY_RATE
            if b.reproduction_cooldown > 0:
                b.reproduction_cooldown -= 1
            if b.energy <= 0:
                b.set_dead()

        for blob, new_pos in new_positions.items():
            blob.pos = new_pos
        return food_consumed

    def new_blob(self, parent1: Optional['Blob'] = None, parent2: Optional['Blob'] = None) -> None:
        if parent1 and parent2:
            parent1.energy = int(parent1.energy / 2)
            parent1.reproduction_cooldown = REPRODUCTION_COOLDOWN
            parent2.energy = int(parent2.energy / 2)
            parent2.reproduction_cooldown = REPRODUCTION_COOLDOWN
            # Find actual blob spawn position between parents
            spawn_position = get_spawn_position(self, self.foodHandler)
            self.blob_list.append(Blob(spawn_position, parent1, parent2))
        else:
            self.blob_list.append(Blob(get_spawn_position(self, self.foodHandler)))

    def check_deaths(self) -> None:
        for b in self.blob_list:
            if not b.alive:
                self.blob_list.remove(b)

    def check_reproduction(self) -> None:
        position_to_blob = {b.pos: b for b in self.blob_list}
        for blob in self.blob_list:
            if not blob.can_reproduce():
                continue

            mate = blob.check_adjacent(position_to_blob)
            if mate:
                self.new_blob(blob, mate)

    def get_blobs(self) -> List[Blob]:
        return self.blob_list

    def get_blob_positions(self) -> List[Tuple[int, int]]:
        return [blob.pos for blob in self.blob_list]