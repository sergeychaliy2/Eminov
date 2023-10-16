import math
import random
import matplotlib.pyplot as mpl
#Гауса
a = 5

SIGMA = math.sqrt(1 / 12)
count = 10000

get_xi = lambda: sum([random.random() for _ in range(12)]) - 6
# xi_list = [SIGMA * get_xi() + a for _ in range(count)]#нормальное распр
xi_list = [get_xi() for _ in range(count)]#стандартное норм распр

sum_values = sum(xi_list)
avg_values = sum_values / count

# print(sum_values, '= [{}, {}]'.format(count * avg_values, count * (SIGMA ** 2)))
# print('[{}, {}]'.format(a - 3 * SIGMA, a + 3 * SIGMA))

mpl.hist(xi_list, bins=100)
mpl.show()
