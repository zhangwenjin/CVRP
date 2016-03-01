from greedy2 import Greedy2
from common.distance import distance


class Greedy4(Greedy2):
    def run(self):
        locations = [self.depot for _ in xrange(self.vehicles_num)]
        current_loads = [self.maximum_load -20 for _ in xrange(self.vehicles_num)]
        paths = [[1] for _ in xrange(self.vehicles_num)]
        sum_distances = [0 for _ in xrange(self.vehicles_num)]
        # iters = [0 for _ in xrange(self.vehicles_num)]

        # for i in xrange(self.vehicles_num):
        #     idx = self.find_nearest(locations[i], current_loads[i])
        #     current_loads[i] -= self.customers[idx].demand
        #     paths[i].append(self.customers[idx].idx)
        #     sum_distances[i] += self.customers[idx].distance(locations[i][0],locations[i][1])
        #     locations[i] = (self.customers[idx].x, self.customers[idx].y)
        #     del self.customers[idx]

        for i in xrange(self.vehicles_num):
            while True:
                idx = self.find_nearest(locations[i], current_loads[i])

                if current_loads == 0:
                    paths[i].append(1)
                    break

                if idx == -1:
                    paths[i].append(1)
                    sum_distances[i] += distance(locations[i], self.depot)
                    break
                current_loads[i] -= self.customers[idx].demand
                paths[i].append(self.customers[idx].idx)
                sum_distances[i] += self.customers[idx].distance(locations[i][0],locations[i][1])
                locations[i] = (self.customers[idx].x, self.customers[idx].y)

                # print i, self.customers[idx].idx
                del self.customers[idx]
        for path in paths:
            print path
        print 'Sum: ', sum(sum_distances)