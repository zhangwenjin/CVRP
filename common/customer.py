import math


class Customer:

    def __init__(self, idx, x, y, demand=0):
        (self.idx, self.x, self.y, self.demand) = (idx, x, y, demand)

    def __str__(self):
        return "Idx: {0}, X: {1}, Y:{2}, Demand: {3}".format(self.idx, self.x, self.y, self.demand)

    def distance2(self, other):
        return math.sqrt(math.fabs((self.x - other.x) ** 2 + (self.y - other.y) ** 2))

    def distance(self, x, y):
        return math.sqrt(math.fabs((self.x - x) ** 2 + (self.y - y) ** 2))

    def set_demand(self, demand):
        self.demand = demand
