from common.algorithm import Algorithm
from math import sqrt, fabs

class Greedy2(Algorithm):
    def __init__(self, input_parameter):
        super(Greedy2, self).__init__(input_parameter)
        self.C = input_parameter.customers[:]
        self.W = []
        self.O = [i + 1 for i in xrange(len(self.customers))]

    def find_min_demand(self):
        min_demand = self.customers[0].demand
        min_node = 0

        for i in xrange(len(self.customers)):
            if min_demand > self.customers[i].demand:
                min_demand = self.customers[i].demand
                min_node = i
        return min_node, min_demand

    def find_nearest(self, location, demand):
        min_distance = 10000
        min_node = -1

        for c in xrange(len(self.customers)):
            tmp = self.customers[c].distance(location[0], location[1])
            if min_distance > tmp and self.customers[c].demand <= demand:
                min_distance = tmp
                min_node = c
        return min_node

    def run(self):
        for i in xrange(self.vehicles_num):
            location = self.depot
            current_load = self.maximum_load
            path = [0]
            sum_distance = 0
            while True:
                if current_load == 0:
                    break
                customer = self.find_nearest(location, current_load)
                if customer == -1:
                    path.append(0)
                    sum_distance += sqrt(fabs((location[0] - self.depot[0])**2 - (location[1] - self.depot[1])**2))
                    break
                path.append(self.customers[customer].idx)
                current_load -= self.customers[customer].demand
                sum_distance += self.customers[customer].distance(location[0], location[1])
                location = (self.customers[customer].x, self.customers[customer].y)
                del self.customers[customer]
            print path, sum_distance
