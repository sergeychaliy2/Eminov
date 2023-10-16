import math
import sympy
import random
import prettytable


def get_xi_list(count: int, from_var: sympy.Symbol, xi_function: sympy.Eq) -> list[float]:
    return [xi_function.subs(from_var, random.random()).evalf() for _ in range(count)]


def choose_best_function(xi_functions: list[sympy.Eq], from_var: sympy.Symbol, target:
        float) -> sympy.Eq | None:
    for eq in xi_functions:
        eq_result = (1 / 5) * sum(get_xi_list(5, from_var, eq))
        if type(eq_result) is sympy.Float:
            try:
                if target >= eq_result - 1.0 and target <= eq_result + 1.0:
                    return eq
            except Exception:
                continue
    return None


m, g = 0, 0
# a, b = 1, 4
a, b = 0, math.pi / 4
N, q = 1000, 10

step = 500

x = sympy.symbols('x', real=True)
f = sympy.symbols('ri', real=True)

# function = 1 / (2 * x ** 0.5)
function = 1 / (sympy.cos(x) ** 2)

primitive_function = sympy.integrate(function, (x, a, x))
reverse_primitive_functions = sympy.solve(f - primitive_function, x)

if len(reverse_primitive_functions) == 0:
    print('Cant solve reverse primitive function')
else:
    M = sympy.integrate(x * function, (x, a, b))
    D = sympy.integrate(x ** 2 * function, (x, a, b)) - M ** 2

    best_function = choose_best_function(reverse_primitive_functions, f, M)

    if best_function is None:
        print('Cant solve reverse primitive function')
        exit(0)

    print('========= FUNC =========')

    print('F(x) =', primitive_function)
    print('G(ri) =', best_function)

    table = prettytable.PrettyTable()
    table.field_names = ['N', 'MX', 'm', '|MX-m|', 'DX', 'g', '|DX-g|']

    xi, xi_d = [], []
    for i in range(step, N + 1, step):
        new_xi = get_xi_list(step, f, best_function)
        new_xi_d = [xk ** 2 for xk in new_xi]

        xi = xi + new_xi
        xi_d = xi_d + new_xi_d

        m = sum(xi) / i
        g = sum(xi_d) / (i - 1) - i / (i - 1) * m ** 2

        table.add_row([i, M, m, abs(M - m), D, g, abs(D - g)])

    print('========= STAT =========')

    print('M =', M)
    print('D =', D)

    print('m =', m)
    print('g =', g)

    print('|M - m| =', abs(M - m))
    print('|D - g| =', abs(D - g))

    print('========= TABLE =========')

    print(table)
