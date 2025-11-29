BLOB_DIRS = {
    0: "🡹",
    1: "🡽",
    2: "🡺",
    3: "🡾",
    4: "🡻",
    5: "🡿",
    6: "🡸",
    7: "🡼"
}

DIR_MOVEMENTS = {
    0: (0, -1),
    1: (1, -1),
    2: (1, 0),
    3: (1, 1),
    4: (0, 1),
    5: (-1, 1),
    6: (-1, 0),
    7: (-1, -1)
}

INITIAL_BLOBS = 15
INITIAL_FOOD = 20

MIN_FOOD = 15
MAX_FOOD = 35
FOOD_SPAWN_PROBABILITY = 0.35

ENERGY_DECAY_RATE = 1.5
ENERGY_ON_CONSUMPTION = 75
MAX_ENERGY = 200

REPRODUCTION_ENERGY_MIN = 150
REPRODUCTION_COOLDOWN = 50

UPDATE_RATE = 0.5

FOOD = "⬤"
EMPTY = " "
WIDTH = 25
HEIGHT = 25