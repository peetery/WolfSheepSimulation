import math

class Animal:
    def __init__(self, x=0.0, y=0.0):
        self.position = (x, y)

    def move(self, distance, direction=None):
        pass

    def get_position(self):
        return self.position

    def distance_to(self, other):
        x1, y1 = self.position
        x2, y2 = other.position
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)