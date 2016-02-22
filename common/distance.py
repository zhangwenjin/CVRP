class DistanceCalculator(object):
    def get_all_distance(self):
        pass

    def get_distance(self, customer1, customer2):
        pass

    def __init__(self, customers):
        self.customers = customers


class Floyd(DistanceCalculator):
    def calculate(self):
        size = len(self.customers)
        for k in xrange(size):
            for i in xrange(size):
                for j in xrange(size):
                    tmp = self.customers[i].distance(self.customers[j])
                    if self.distances[i][j] > tmp:
                        self.distances[i][j] = tmp

    def get_all_distance(self):
        return self.distances

    def get_distance(self, customer1_idx, customer2_idx):
        return self.distances[customer1_idx][customer2_idx]

    def __init__(self, customers):
        super(Floyd, self).__init__(customers)
        self.distances = [[999999999 for _ in range(len(customers))] for _ in range(len(customers))]


class Euclidean(DistanceCalculator):
    def calculate(self):
        size = len(self.customers)
        for i in xrange(size):
            for j in xrange(size):
                self.distances[i][j] = self.customers[i].distance(self.customers[j])

    def get_all_distance(self):
        return self.distances

    def get_distance(self, customer1_idx, customer2_idx):
        return self.distances[customer1_idx][customer2_idx]

    def __init__(self, customers):
        super(Floyd, self).__init__(customers)
        self.distances = [[0 for _ in range(len(customers))] for _ in range(len(customers))]




