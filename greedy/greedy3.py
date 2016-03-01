from greedy2 import Greedy2
from common.distance import distance


class Greedy3(Greedy2):
    def run(self):
        locations = [self.depot for _ in xrange(self.vehicles_num)]
        current_loads = [self.maximum_load -20 for _ in xrange(self.vehicles_num)]
        paths = [[0] for _ in xrange(self.vehicles_num)]
        sum_distances = [0 for _ in xrange(self.vehicles_num)]
        for i in xrange(self.vehicles_num):
            customer = self.find_nearest(locations[i], current_loads[i])
            paths[i].append(self.customers[customer].idx)
            current_loads[i] -= self.customers[customer].demand
            sum_distances[i] += self.customers[customer].distance(locations[i][0], locations[i][1])
            locations[i] = (self.customers[customer].x, self.customers[customer].y)
            del self.customers[customer]
        while True:
            if len(self.customers) == 0:
                break
            for i in xrange(self.vehicles_num):
                customer = self.find_nearest(locations[i], current_loads[i])

                if customer == -1 or current_loads[i] == 0:
                    paths[i].append(0)
                    sum_distances[i] += distance(locations[i], self.depot)
                    continue
                paths[i].append(self.customers[customer].idx)
                current_loads[i] -= self.customers[customer].demand
                sum_distances[i] += self.customers[customer].distance(locations[i][0], locations[i][1])
                locations[i] = (self.customers[customer].x, self.customers[customer].y)
                del self.customers[customer]
        for path in paths:
            print path
        for sum_distance in sum_distances:
            print sum_distance
        print 'Sum is :' , sum(sum_distances)