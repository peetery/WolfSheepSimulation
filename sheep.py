import random

from animal import Animal


class Sheep(Animal):
    def __init__(self, x, y, move_distance=0.5):
        super().__init__(x, y, move_distance)
        self.alive = True

    def move(self):
        directions = {
            "north": (0, self.move_distance),
            "south": (0, -self.move_distance),
            "east": (self.move_distance, 0),
            "west": (-self.move_distance, 0)
        }
        direction = random.choice(list(directions.values()))
        x, y = self.position
        self.position = (x + direction[0], y + direction[1])

    def die(self):
        self.alive = False
        self.position = None