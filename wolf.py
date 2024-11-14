import math
from typing import override

from animal import Animal


class Wolf(Animal):
    def __init__(self, move_distance=1.0):
        super().__init__(0.0, 0.0)
        self.move_distance = move_distance

    def find_closest_sheep(self, sheep_list):
        closest_sheep = None
        closest_distance = float("inf")
        for sheep in sheep_list:
            distance = self.squared_distance_to(sheep)
            if distance < closest_distance:
                closest_sheep = sheep
                closest_distance = distance
        return closest_sheep, closest_distance

    def move(self, target=None):
        if target is None:
            return
        x1, y1 = self.position
        x2, y2 = target.position
        distance_sq = self.squared_distance_to(target)
        if distance_sq <= self.move_distance ** 2:
            self.position = target.position
        else:
            direction = ((x2 - x1) / math.sqrt(distance_sq), (y2 - y1) / math.sqrt(distance_sq))
            self.position = (x1 + direction[0] * self.move_distance, y1 + direction[1] * self.move_distance)