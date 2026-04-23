import copy
from typing import TypeVar, Generic

from entities.base import MathField

T = TypeVar('T', bound='MathField')

class SystemSolver(Generic[T]):
    def __init__(self, a: list[list[T]], b: list[T]) -> None:
        self.a = a
        self.b = b

    @staticmethod
    def gauss_method(a, b) -> tuple[list[T] | None, list[T]]:
        m, n = len(a), len(a[0])

        zero = a[0][0].get_zero()

        mat = [a[i][:] + [b[i]] for i in range(m)]

        pivots = []
        row = 0

        for col in range(n):
            pivot = None

            for r in range(row, m):
                if mat[r][col] != zero:
                    pivot = r
                    break

            if pivot is None:
                continue

            mat[row], mat[pivot] = mat[pivot], mat[row]


            pivot_val = mat[row][col]

            for j in range(col, n + 1):
                mat[row][j] = mat[row][j] / pivot_val

            for r in range(row + 1, m):
                factor = mat[r][col]
                if factor != zero:
                    for j in range(col, n + 1):
                        mat[r][j] = mat[r][j] - factor * mat[row][j]

            pivots.append(col)
            row += 1

            if row == m:
                break

        # проверка несовместности
        for r in range(row, m):
            if all(mat[r][c] == zero for c in range(n)) and mat[r][n] != zero:
                return None, pivots

        # back substitution
        x = [zero for _ in range(n)]

        for i in reversed(range(len(pivots))):
            r = i
            col = pivots[i]

            val = mat[r][n]

            for j in range(col + 1, n):
                val = val - mat[r][j] * x[j]

            x[col] = val

        return x, pivots