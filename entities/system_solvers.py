from typing import TypeVar, Generic

from entities.base import MathField

T = TypeVar('T', bound='MathField')

class SystemSolver(Generic[T]):
    def __init__(self, A: list[list[T]], b: list[T]) -> None:
        self.A = A
        self.b = b

    @staticmethod
    def gauss_method(a, b) -> tuple[list[T] | None, list[T]]:
        """
        Решает A x = b над GF(p)
        Возвращает:
            x        — частное решение (список длины n) или None, если нет решений
            pivots   — список индексов ведущих столбцов
        """
        m, n = len(a), len(a[0])
        zero = type(a[0][0]).zero()

        # расширенная матрица
        extended_a = [a[i] + [b[i]] for i in range(m)]

        row = 0
        pivots = []

        for col in range(n):
            pivot = None
            for r in range(row, m):
                if extended_a[r][col] != 0:
                    pivot = r
                    break
            if pivot is None:
                continue

            extended_a[row], extended_a[pivot] = extended_a[pivot], extended_a[row]

            for j in range(col, n + 1):
                extended_a[row][j] = extended_a[row][j] / extended_a[row][col]

            # 4. обнуление остальных строк
            for r in range(m):
                if r != row and extended_a[r][col] != 0:
                    factor = extended_a[r][col]
                    for j in range(col, n + 1):
                        extended_a[r][j] = (extended_a[r][j] - factor * extended_a[row][j])

            pivots.append(col)
            row += 1
            if row == m:
                break

        # 5. проверка на несовместность
        for r in range(row, m):
            if all(extended_a[r][c] == 0 for c in range(n)) and extended_a[r][n] != 0:
                return None, pivots  # нет решений

        # 6. восстановление решения (свободные переменные = 0)
        x = [0] * n
        for r, col in enumerate(pivots):
            x[col] = extended_a[r][n]

        return x, pivots