from common.algorithm import Algorithm
from common.distance import distance


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

        for c in xrange(1, len(self.customers)):
            tmp = self.customers[c].distance(location[0], location[1])
            if min_distance > tmp and self.customers[c].demand <= demand:
                min_distance = tmp
                min_node = c
        return min_node

    def run(self):
        min_demand = min([c.demand for c in self.customers[1:]])
        s = 0
        locations = [self.depot for _ in xrange(self.vehicles_num)]
        current_loads = [self.maximum_load for _ in xrange(self.vehicles_num)]
        paths = [[1] for _ in xrange(self.vehicles_num)]
        sum_distances = [0 for _ in xrange(self.vehicles_num)]
        # for _ in xrange(1):
        #     for i in xrange(self.vehicles_num):
        #         customer = self.find_nearest(locations[i], current_loads[i])
        #         if customer == -1:
        #             continue
        #         paths[i].append(self.customers[customer].idx)
        #         current_loads[i] -= self.customers[customer].demand
        #         sum_distances[i] += self.customers[customer].distance(locations[i][0], locations[i][1])
        #         locations[i] = (self.customers[customer].x, self.customers[customer].y)
        #         del self.customers[customer]

        for i in xrange(self.vehicles_num):
            location = locations[i]
            current_load = current_loads[i]
            path = paths[i]
            sum_distance = sum_distances[i]
            while True:
                customer = self.find_nearest(location, current_load)
                if customer == -1 or current_load == 0:
                    path.append(1)
                    sum_distance += distance(location, self.depot)
                    break
                path.append(self.customers[customer].idx)
                current_load -= self.customers[customer].demand
                sum_distance += self.customers[customer].distance(location[0], location[1])
                location = (self.customers[customer].x, self.customers[customer].y)
                del self.customers[customer]
            print path, sum_distance
            s += sum_distance
        print 'Sum is :', s
