import math


class Customer:

    def __init__(self, idx, x, y, demand):
        (self.idx, self.x, self.y, self.demand) = (idx, x, y, demand)

    def __str__(self):
        return "Idx: {0}, X: {1}, Y:{2}, Demand: {3}".format(self.idx, self.x, self.y, self.demand)

    def distance(self, other):
        return math.sqrt(self.x ** 2 + self.y ** 2 - other.x ** 2 + other.y **2)