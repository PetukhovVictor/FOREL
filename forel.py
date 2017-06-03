import numpy as np
import random

class Forel:
    def __init__(self, data):
        self.data = data

    def get_rand_object(self):
        if len(self.data) == 0:
            return None
        index = random.randint(0, len(self.data) - 1)
        rand_object = self.data[index]
        self.data = np.delete(self.data, index, 0)
        return rand_object

    def clustering_not_finish(self):
        return len(self.data) != 0
