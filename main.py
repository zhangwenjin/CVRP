from common.reader import Reader
from greedy.greedy2 import Greedy2
from common.parameter import InputParameter
from matplotlib import pyplot


def plot(x, y, color='b', marker='o'):
    pyplot.plot(x, y, marker + color)
    pyplot.xlim(min(x) - 1, max(x) + 1)
    pyplot.ylim(min(y) - 1, max(y) + 1)


f = open('input/P/P-n65-k10=792.vrp', 'r')
r = Reader(f)
r.read()
c = r.get_customers()
for i in c:
    print i

x_points = []
y_points = []

for i in range(len(c)):
    x_points.append(c[i].x)
    y_points.append(c[i].y)
plot(x_points, y_points, color='b', marker='o')

pyplot.show()

print '---------------------------'
input_param = InputParameter(c, r.get_depot(), r.get_vehicles_num(), r.get_maximum_load())
greedy = Greedy2(input_param)
last = greedy.run()
summ = 0
for i in c:
    summ += i.demand

print '==============='
print summ

