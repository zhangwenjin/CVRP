from common.algorithm import Algorithm


class Greedy(Algorithm):
    def __init__(self, input_parameter):
        super(Greedy, self).__init__(input_parameter)
        self.C = input_parameter.customers[:]
        self.depot = input_parameter.depot
        self.maximum_load = input_parameter.maximum_load
        self.vehicles_num = input_parameter.vehicles_num
        self.W = []
        self.O = [i + 1 for i in xrange(len(self.customers))]

    def run(self):
        last_point = [0 for i in xrange(2 * self.vehicles_num)]
        for i in xrange(len(last_point)):
            min_dis = self.C[self.O[0]].distance(self.depot[0], self.depot[1])
            min_node = self.O[0]
            for j in xrange(1, len(self.O) - 1):
                tmp = self.C[self.O[j]].distance(self.depot[0], self.depot[1])
                if min_dis > tmp:
                    min_dis = tmp
                    min_node = self.O[j]
            last_point[i] = min_node
            self.O.remove(min_node)



