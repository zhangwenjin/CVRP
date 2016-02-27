class Algorithm(object):
    def __init__(self, input_parameter):
        self.customers = input_parameter.customers
        self.depot = input_parameter.depot
        self.vehicles_num = input_parameter.vehicles_num
        self.maximum_load = input_parameter.maximum_load
        self.output_parameter = None

    def run(self):
        return self.output_parameter
