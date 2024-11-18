from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, x=0.0, y=0.0, move_distance=1.0):
        self.position = (x, y)
        self.move_distance = move_distance

    @abstractmethod
    def move(self):
        pass

    def get_position(self):
        return self.position

    def squared_distance_to(self, other):
        x1, y1 = self.position
        x2, y2 = other.position
        return (x1 - x2) ** 2 + (y1 - y2) ** 2