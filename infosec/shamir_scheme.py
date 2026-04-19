import random

from entities.finite_field import Zp
from entities.polynomial import Polynomial
from utils import next_prime

M = 91319049123812903912391238912031231239

k = 300
n = 500

p = next_prime(M)

coefs = []
coefs.append(Zp(value=M, p=p))
for _ in range(k - 2):
    coefs.append(Zp(value=random.randint(0, p), p=p))
coefs.append(Zp(value=random.randint(1, p), p=p))
pol = Polynomial(coefs)

f = lambda x: pol.evaluate(x)

known_secrets = random.sample(range(1, n + 1), k)
known_secrets_values = [f(Zp(value=x, p=p)) for x in known_secrets]

pol2 = Polynomial([Zp(0, p)])
l_matrix = [[0] * k for _ in range(k)]

for i in range(k):
    l_i = Polynomial([Zp(value=1, p=p)])

    for j in range(k):
        if i != j:
            inv = Zp(value=known_secrets[i] - known_secrets[j], p=p).inverse()
            r = Polynomial([Zp(value=-known_secrets[j], p=p), Zp(value=1, p=p)]).scale(inv)
            l_i = l_i * r

    for idx in range(len(l_i.coefficients)):
        l_matrix[idx][i] = l_i.coefficients[idx]

    scaled = l_i * Polynomial([known_secrets_values[i]])
    pol2 = pol2 + scaled

print("Original polynomial:", pol, "...", pol)
print("Reconstructed:", pol2, "...", pol2)
print("Equal:", pol2 == pol)