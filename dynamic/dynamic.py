from common.algorithm import Algorithm
from common.customer import Customer
from common.distance import Euclidean
from common.parameter import InputParameter
from math import log
from common.distance import distance


class Dynamic(Algorithm):

    def run(self):
        locations = [self.depot for _ in xrange(self.vehicles_num)]
        current_loads = [self.maximum_load for _ in xrange(self.vehicles_num)]
        paths = [[1] for _ in xrange(self.vehicles_num)]
        sum_distances = [0 for _ in xrange(self.vehicles_num)]

        dist = Euclidean(self.customers)
        dist.calculate()
        n = len(self.customers )
        dist = dist.get_all_distance()
        best = [[1000000 for _ in xrange(n)] for _ in xrange(1 << n)]
        best[1][0] = 0
        set_range = range(1, 1 << n, 2)
        for mask in set_range:
            for i in xrange(1, n):
                if (mask & 1 << i) != 0:
                    for j in xrange(n):
                        if (mask & 1 << j) != 0:
                            best[mask][i] = min(best[mask][i], best[mask ^ (1 << i)][j] + dist[j][i])

        subset = (1 << n) - 1
        tour = [0 for _ in xrange(n)]
        last = 0
        set_range = xrange(n - 1, 0, -1)
        idx = 1
        for i in set_range:
            bj = -1
            for j in xrange(1, n):
                if (subset & 1 << j) != 0 and \
                        (bj == -1 or best[subset][bj] + dist[bj][last] > best[subset][j] + dist[j][last]):
                    bj = j

            tour[i] = bj
            subset ^= 1 << bj
            last = bj
        print tour
        for i in xrange(self.vehicles_num):
            print idx
            while idx < n and current_loads[i] - self.customers[tour[idx]].demand > 0 :
                paths[i].append(self.customers[tour[idx]].idx)
                sum_distances[i] += distance(locations[i], (self.customers[tour[idx]].x, self.customers[tour[idx]].y))
                current_loads[i] -= self.customers[tour[idx]].demand
                locations[i] = (self.customers[tour[idx]].x, self.customers[tour[idx]].y)
                idx += 1
            paths[i].append(self.customers[0].idx)
            sum_distances[i] += distance(locations[i], (self.customers[0].x, self.customers[0].y))
        for i in xrange(self.vehicles_num):
            print paths[i], sum_distances[i]
        print 'Sum :', sum(sum_distances), n
