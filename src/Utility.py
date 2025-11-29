import random as r
from typing import Tuple, Optional, TYPE_CHECKING
from constants import WIDTH, HEIGHT
if TYPE_CHECKING:
    from BlobHandler import BlobHandler
    from FoodHandler import FoodHandler

def get_random_color() -> Tuple[int, int, int]:
    red = r.randrange(0, 255)
    green = int(r.randrange(0, 255) / 5)
    blue = r.randrange(0, 255)
    color = (red, green, blue)
    return color

def blend_colors(color1: Tuple[int, int, int], color2: Tuple[int, int, int]) -> Tuple[int, int, int]:
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    newR = int((r1 + r2) / 2)
    newG = int((g1 + g2) / 2)
    newB = int((b1 + b2) / 2)
    return (newR, newG, newB)

def get_spawn_position(blobHandler: Optional['BlobHandler'], foodHandler: Optional['FoodHandler']) -> Tuple[int, int]:
    blob_positions = blobHandler.get_blob_positions()
    food_positions = foodHandler.get_food_positions()
    while True:
        new_pos = (r.randrange(WIDTH), r.randrange(HEIGHT))
        if new_pos not in blob_positions and new_pos not in food_positions:
            return new_pos