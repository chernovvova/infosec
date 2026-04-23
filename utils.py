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


def mod_inv(a, p):
    # обратный элемент в GF(p), p — простое
    # a != 0 mod p
    return pow(a, p - 2, p)


def mod_gauss_method(A, b, p):
    """
    Решает A x = b над GF(p)
    Возвращает:
        x        — частное решение (список длины n) или None, если нет решений
        pivots   — список индексов ведущих столбцов
    """
    # копии, всё сразу нормализуем
    A = [row[:] for row in A]
    b = b[:]
    m, n = len(A), len(A[0])

    # расширенная матрица
    aug = [A[i] + [b[i]] for i in range(m)]

    row = 0
    pivots = []

    for col in range(n):
        # 1. поиск pivot
        pivot = None
        for r in range(row, m):
            if aug[r][col] % p != 0:
                pivot = r
                break
        if pivot is None:
            continue

        # 2. swap
        aug[row], aug[pivot] = aug[pivot], aug[row]

        # 3. нормализация строки (делаем pivot = 1)
        inv = mod_inv(aug[row][col] % p, p)
        for j in range(col, n + 1):
            aug[row][j] = (aug[row][j] * inv) % p

        # 4. обнуление остальных строк
        for r in range(m):
            if r != row and aug[r][col] % p != 0:
                factor = aug[r][col] % p
                for j in range(col, n + 1):
                    aug[r][j] = (aug[r][j] - factor * aug[row][j]) % p

        pivots.append(col)
        row += 1
        if row == m:
            break

    # 5. проверка на несовместность
    for r in range(row, m):
        if all(aug[r][c] % p == 0 for c in range(n)) and aug[r][n] % p != 0:
            return None, pivots  # нет решений

    # 6. восстановление решения (свободные переменные = 0)
    x = [0] * n
    for r, col in enumerate(pivots):
        x[col] = aug[r][n] % p

    return x, pivots


def matrix_production(A, B):
    m, k = len(A), len(A[0])

    # определяем: матрица или вектор
    is_matrix = isinstance(B[0], (list, tuple))
    if is_matrix:
        zero = B[0][0].get_zero()
    else:
        zero = B[0].get_zero()

    if is_matrix:
        k2, n = len(B), len(B[0])
        if k != k2:
            raise ValueError("Incompatible matrix sizes")

        C = [[zero for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for t in range(k):
                a_it = A[i][t]
                for j in range(n):
                    C[i][j] = C[i][j] + a_it * B[t][j]

        return C

    else:
        # B — вектор
        if len(B) != k:
            raise ValueError("Incompatible matrix-vector sizes")

        result = [zero for _ in range(m)]

        for i in range(m):
            s = zero
            for j in range(k):
                s = s + A[i][j] * B[j]
            result[i] = s

        return result