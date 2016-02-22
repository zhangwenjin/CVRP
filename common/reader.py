from customer import Customer


class Reader:

    def __init__(self, input_file):
        self.file = input_file
        self.vehicles_num = 0
        self.customers_num = 0
        self.maximum_load = 0
        self.customers = []
        self.depot = (0, 0)

    def get_customers(self):
        return self.customers

    def get_vehicles_num(self):
        return self.vehicles_num

    def get_customers_num(self):
        return self.customers_num

    def get_maximum_load(self):
        return self.maximum_load

    def get_depot(self):
        return self.depot

    def read(self):
        line = self.file.readline()
        (vehicles_num, customers_num, maximum_load) = [t(s) for t, s in zip((int, int, float), line.split())]
        self.vehicles_num = vehicles_num
        self.customers_num = customers_num
        self.maximum_load = maximum_load

        print(self.file.readline())
        for c in range(customers_num):
            line = self.file.readline()
            (idx, x, y) = [t(s) for t, s in zip((int, float, float), line.split())]
            customer = Customer(idx, x, y)
            self.customers.append(customer)
        print(self.file.readline())
        for c in range(customers_num):
            line = self.file.readline()
            (idx, demand) = [t(s) for t, s in zip((int, float), line.split())]
            self.customers[c].set_demand(demand)
        print(self.file.readline())
        x = int(self.file.readline())
        y = int(self.file.readline())

        self.depot = (x, y)
        print (self.file.readline())



