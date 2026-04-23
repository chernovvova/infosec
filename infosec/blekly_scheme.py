import random

from entities.finite_field import Zp
from solvers.system_solvers import SystemSolver
from utils import next_prime, matrix_production


def generate_random_zp_matrix(n, m, p):
    a = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(Zp(random.randint(0, p - 1),p))
        a.append(row)

    return a


M = 1231312312389127389127312893
n = 150
k = 150

p = next_prime(M)

coords = [Zp(M, p)] + [Zp(random.randint(0, p - 1 ), p) for _ in range(k - 1)]
a = generate_random_zp_matrix(k, n, p)
b = matrix_production(a, coords)

solution = SystemSolver.gauss_method(a, b)
print(coords, solution)

