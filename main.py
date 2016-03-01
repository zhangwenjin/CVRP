from common.reader import Reader
from greedy.greedy3 import Greedy3
from greedy.greedy2 import Greedy2
from greedy.greedy4 import Greedy4
from greedy.greedy5 import Greedy5
from dynamic.dynamic import Dynamic

from common.parameter import InputParameter
from matplotlib import pyplot


def plot(x, y, color='b', marker='o'):
    pyplot.plot(x, y, marker + color)
    pyplot.xlim(min(x) - 1, max(x) + 1)
    pyplot.ylim(min(y) - 1, max(y) + 1)


f = open('input/P/test.vrp', 'r')
r = Reader(f)
r.read()
c = r.get_customers()


x_points = []
y_points = []

for i in range(len(c)):
    x_points.append(c[i].x)
    y_points.append(c[i].y)
plot(x_points, y_points, color='b', marker='o')

pyplot.show()

print '---------------------------'
input_param = InputParameter(c, r.get_depot(), r.get_vehicles_num(), r.get_maximum_load())
greedy = Greedy5(input_param)
last = greedy.run()

