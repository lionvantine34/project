import random

class RNG:
    def __init__(self, seed=None):
        self.random = random.Random(seed)

    def randint(self, a, b):
        return self.random.randint(a, b)

    def random_float(self):
        return self.random.random()
