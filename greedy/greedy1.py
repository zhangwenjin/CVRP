from common.algorithm import Algorithm


class Greedy(Algorithm):
    def __init__(self, input_parameter):
        super(Greedy, self).__init__(input_parameter)
        self.C = input_parameter.customers[:]
        self.W = []
        self.O = [i + 1 for i in xrange(len(self.customers))]

    def run(self):
        self.W = []
        for i in xrange(2 * self.vehicles_num):
            min_dis = self.C[self.O[0]].distance(self.depot[0], self.depot[1])
            min_node = self.O[0]
            for j in xrange(1, len(self.O) - 1):
                tmp = self.C[self.O[j]].distance(self.depot[0], self.depot[1])
                if min_dis > tmp:
                    min_dis = tmp
                    min_node = self.O[j]
            self.W.append(min_node)
            self.O.remove(min_node)
        return self.W

    def run2(self):
        for j in xrange(len(self.O)):
            min_dis = self.C[self.O[j]].distance(self.C[self.W[0]][0], self.C[self.W[0]][1])
            min_node = self.O[0]
            for w in xrange(len(self.W)):
                tmp = self.C[self.O[j]].distance(self.C[self.W[w]][0], self.C[self.W[w]][1])
                if min_dis > tmp:
                    min_dis = tmp
                    min_node = w
            self.W.append(min_node)
            self.O.remove(min_node)
        return self.W


