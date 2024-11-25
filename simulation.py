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
        self.pos_data = []
        self.alive_data = []

    def run(self):
        for self.round_no in range(1, self.max_rounds + 1):
            print(f"\nRound {self.round_no}:")
            self.run_round()

            alive_sheep_count = len([sheep for sheep in self.sheep if sheep.alive])
            print(f"Wolf at ({self.wolf.get_position()[0]:.3f},"
                  f" {self.wolf.get_position()[1]:.3f}), Alive sheep: {alive_sheep_count}")

            self.save_round_data()

            if alive_sheep_count == 0:
                print("\nAll sheep have been eaten. Simulation ended.")
                break
            elif self.round_no == self.max_rounds:
                print("\nMax rounds reached. Simulation ended.")
                break

    def run_round(self):
        for sheep in self.sheep:
            if sheep.alive:
                sheep.move()

        closest_sheep, closest_distance = self.wolf.find_closest_sheep(self.sheep)
        if closest_sheep:
            sheep_index = self.sheep.index(closest_sheep)
            if closest_distance <= self.wolf.move_distance ** 2:
                print(f"Wolf eats sheep {sheep_index}")
                self.wolf.move(target=closest_sheep)
                closest_sheep.die()
            else:
                print(f"Wolf chases sheep {sheep_index}")
                self.wolf.move(target=closest_sheep)

    def save_round_data(self):
        self.pos_data.append({
            'round_no': self.round_no,
            'wolf_pos': self.wolf.get_position(),
            'sheep_pos': [sheep.get_position() if sheep.alive else None for sheep in self.sheep]
        })

        alive_sheep_count = len([sheep for sheep in self.sheep if sheep.alive])
        self.alive_data.append([self.round_no, alive_sheep_count])

        if self.round_no == self.max_rounds or alive_sheep_count == 0:
            save_to_json(self.pos_data)
            save_to_csv(self.alive_data)
