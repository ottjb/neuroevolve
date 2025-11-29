import random as r
from Food import Food
from BlobHandler import BlobHandler
from typing import Optional, List, Tuple
from Utility import get_spawn_position
from constants import WIDTH, HEIGHT, FOOD_SPAWN_PROBABILITY, MIN_FOOD

class FoodHandler():
    def __init__(self, blobHandler: Optional['BlobHandler']):
        self.food_list = []
        self.blobHandler = blobHandler

    def new_food(self) -> None:
        self.food_list.append(Food(get_spawn_position(self.blobHandler, self)))

    def remove_food(self, food: Optional['Food']) -> None:
        self.food_list.remove(food)

    def spawn_food(self) -> None:
        while len(self.food_list) < MIN_FOOD:
            self.new_food()
        x = r.random()
        if x <= FOOD_SPAWN_PROBABILITY:
            self.new_food()
    
    def get_food_positions(self) -> List[Tuple[int, int]]:
        return [food.pos for food in self.food_list]
    
    def get_food_list(self) -> List[Food]:
        return self.food_list