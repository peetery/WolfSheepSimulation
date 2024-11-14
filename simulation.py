import random

from wolf import Wolf
from sheep import Sheep
from utils import save_to_json, save_to_csv


class Simulation:
    def __init__(self, num_sheep=15, max_rounds=50, sheep_move_dist=0.5,
                 wolf_move_dist=1.0, init_pos_limit=10.0, wolf_x=0.0, wolf_y=0.0):
        self.round_no = 0
        self.max_rounds = max_rounds
        self.wolf = Wolf(x=wolf_x, y=wolf_y, move_distance=wolf_move_dist)
        self.sheep = [
            Sheep(x = random.uniform(-init_pos_limit, init_pos_limit),
                  y = random.uniform(-init_pos_limit, init_pos_limit),
                  move_distance = sheep_move_dist)
            for _ in range(num_sheep)
        ]

    def run(self):
        pos_data = []
        alive_data = []

        while self.sheep and self.round_no < self.max_rounds:
            self.round_no += 1
            print(f"Round {self.round_no}")

            for sheep in self.sheep:
                sheep.move()

            closest_sheep, closest_distance = self.wolf.find_closest_sheep(self.sheep)
            if closest_sheep:
                if closest_distance <= self.wolf.move_distance ** 2:
                    print(f"Wolf eats sheep at position {closest_sheep.get_position()}")
                    self.wolf.move(target=closest_sheep)
                    self.sheep.remove(closest_sheep)
                else:
                    print(f"Wolf chases sheep at position {closest_sheep.get_position()}")
                    self.wolf.move(target=closest_sheep)

            pos_data.append({
                'round_no': self.round_no,
                'wolf_pos:': self.wolf.get_position(),
                'sheep_pos': [sheep.get_position() if sheep in self.sheep else None for sheep in self.sheep]
            })

            alive_data.append((self.round_no, len(self.sheep)))

            print(f"Wolf position: {self.wolf.get_position()}")
            print(f"Number of sheep alive: {len(self.sheep)}")

            save_to_json(pos_data)
            save_to_csv(alive_data)