import math

from animal import Animal


class Wolf(Animal):
    def __init__(self, x=0.0, y=0.0, move_distance=1.0):
        super().__init__(x, y, move_distance)

    def find_closest_sheep(self, sheep_list):
        living_sheep = [sheep for sheep in sheep_list if sheep.alive]
        if not living_sheep:
            return None
        else:
            closest_sheep = None
            closest_distance = float("inf")
            for sheep in living_sheep:
                distance = self.squared_distance_to(sheep)
                if distance < closest_distance:
                    closest_sheep = sheep
                    closest_distance = distance
            return closest_sheep, closest_distance

    def move(self, target=None):
        if target is None:
            return
        wx, wy = self.position
        tx, ty = target.position
        distance_sq = self.squared_distance_to(target)
        if distance_sq <= self.move_distance ** 2:
            self.position = target.position
        else:
            distance = math.sqrt(distance_sq)
            factors = ((tx - wx) / distance, (ty - wy) / distance)
            self.position = (wx + factors[0] * self.move_distance, wy + factors[1] * self.move_distance)