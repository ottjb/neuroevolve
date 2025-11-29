import random as r

class Brain():
    def __init__(self):
        pass

    def next_move(self) -> int:
        options = [0, 1, 2, 2, 2, 2, 3, 4]
        return r.choice(options)