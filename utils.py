import random


def mod_inverse(a, p):
    """Алгоритм Евклида, нахождение обратного элемента по модулю"""
    if a == 0:
        raise ValueError("Для 0 нет обратного элемента")

    t, new_t = 0, 1
    r, new_r = p, a

    while new_r != 0:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r

    if t < 0:
        t += p

    return t


def quick_pow(a: int, n: int, p: int = 1):
    """Быстрое возведение в степень по модулю p"""
    a = a % p
    result = 1

    while n > 0:
        if n % 2 == 1:
            result = (result * a) % p

        a = (a * a) % p
        n //= 2

    return result

def miller_rabin(n: int, rounds: int = 40) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(rounds):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False

    return True


def next_prime(n: int) -> int:
    if n <= 2:
        return True

    candidate = n if n % 2 else n + 1
    while True:
        if miller_rabin(candidate):
            return candidate
        candidate += 2