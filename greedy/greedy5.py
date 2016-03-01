from greedy2 import Greedy2
from common.distance import distance


class Greedy5(Greedy2):
    def find_farest(self, location, demand):
        min_distance = 0
        min_node = -1

        for c in xrange(len(self.customers)):
            tmp = self.customers[c].distance(location[0], location[1])
            if min_distance < tmp and self.customers[c].demand <= demand:
                min_distance = tmp
                min_node = c
        return min_node

    def run(self):
        locations = [self.depot for _ in xrange(self.vehicles_num)]
        current_loads = [self.maximum_load-20 for _ in xrange(self.vehicles_num)]
        paths = [[1] for _ in xrange(self.vehicles_num)]
        sum_distances = [0 for _ in xrange(self.vehicles_num)]
        iters = [0 for _ in xrange(self.vehicles_num)]

        cent_num = 1
        index = -1
        for i in xrange(self.vehicles_num):
            summ = 0
            for j in xrange(len(self.customers)):
                s = 0
                for cent in xrange(cent_num):
                    temp = self.customers[j].distance(locations[cent][0],locations[cent][1])
                    s += temp
                if s > summ :
                    summ = s
                    index = j

            cent_num += 1
            current_loads[i] -= self.customers[index].demand
            paths[i].append(self.customers[index].idx)
            sum_distances[i] += self.customers[index].distance(locations[i][0],locations[i][1])
            locations[i] = (self.customers[index].x, self.customers[index].y)
            del self.customers[index]

        # for i in xrange(self.vehicles_num):
        #     idx = self.find_farest(locations[i], current_loads[i])
        #     current_loads[i] -= self.customers[idx].demand
        #     paths[i].append(self.customers[idx].idx)
        #     sum_distances[i] += self.customers[idx].distance(locations[i][0],locations[i][1])
        #     locations[i] = (self.customers[idx].x, self.customers[idx].y)
        #     del self.customers[idx]

        for i in xrange(self.vehicles_num):
            while True:
                idx = self.find_nearest(locations[i], current_loads[i])
                if idx == -1 or current_loads[i] == 0:
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