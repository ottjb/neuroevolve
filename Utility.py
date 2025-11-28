import random as r

def get_random_color():
    red = int(r.randint(0, 255) / 2)
    green = int(r.randint(0, 255) / 3)
    blue = r.randint(0, 255)
    color = f"rgb({str(red)},{str(green)},{str(blue)})"
    return color