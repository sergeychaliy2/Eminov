import random
import prettytable
#Моделирование дискретной случайной величины
N, q = 1000, 15

X = [-1,     -2,      25]
p = [0.1,   0.8,    0.1]
d = [0.1,   0.9,    1]
v = [0,     0,      0]
r = [[],   [],     []]

vals_count = len(X)

for i in range(10000):
    rk = random.uniform(0.0, 1.0)
    for j in range(vals_count):
        if d[j] >= rk:
            v[j] += 1
            r[j].append(rk)
            break

v_p = [v_i / sum(v) for v_i in v[:]]
delta = [abs(v_p[i] - p[i]) for i in range(vals_count)]

table = prettytable.PrettyTable()
table.field_names = ['1', '2', '3', '4']
table.header = False

table.add_row(['Случайная величина X', *X], divider=True)
table.add_row(['Вероятность p', *p], divider=True)
table.add_row(['Моделирование', *v_p], divider=True)
table.add_row(['Delta', *delta], divider=True)

print(table)

M = sum([p[i] * X[i] for i in range(vals_count)])
D = sum([p[i] * (X[i] - M) ** 2 for i in range(vals_count)])

m = sum([v_p[i] * X[i] for i in range(vals_count)])
g = sum([v_p[i] * (X[i] - m) ** 2 for i in range(vals_count)])

table = prettytable.PrettyTable()
table.field_names = ['M', 'm', '|M - m|']
table.add_row([M, m, abs(M - m)])
print(table)

table = prettytable.PrettyTable()
table.field_names = ['D', 'g', '|D - g|']
table.add_row([D, g, abs(D - g)])
print(table)
