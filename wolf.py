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

    @override
    def move(self, target_sheep):
        if target_sheep is None:
            return
        x1, y1 = self.position
        x2, y2 = target_sheep.position
        distance = self.squared_distance_to(target_sheep)
        if distance <= self.move_distance ** 2:
            self.position = target_sheep.position
        else:
            direction = ((x2 - x1) / distance ** 0.5, (y2 - y1) / distance ** 0.5)
            self.position = (x1 + direction[0] * self.move_distance, y1 + direction[1] * self.move_distance)