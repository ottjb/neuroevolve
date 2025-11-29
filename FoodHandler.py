import random as r
from Food import Food
from constants import WIDTH, HEIGHT, FOOD_SPAWN_PROBABILITY, MIN_FOOD

class FoodHandler():
    def __init__(self, blobHandler):
        self.food_list = []
        self.blobHandler = blobHandler

    def new_food(self):
        blob_positions = self.blobHandler.get_blob_positions()
        food_positions = self.get_food_positions()
        while True:
            new_pos = (r.randrange(WIDTH), r.randrange(HEIGHT))
            if new_pos not in blob_positions and new_pos not in food_positions:
                self.food_list.append(Food(new_pos))
                break

    def remove_food(self, food):
        self.food_list.remove(food)

    def spawn_food(self):
        while len(self.food_list) < MIN_FOOD:
            self.new_food()
        x = r.random()
        if x <= FOOD_SPAWN_PROBABILITY:
            self.new_food()
    
    def get_food_positions(self):
        return [food.pos for food in self.food_list]
    
    def get_food_list(self):
        return self.food_list