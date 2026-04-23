from typing import TypeVar, Generic

from entities.base import MathField

T = TypeVar('T', bound=MathField)

class Matrix(Generic[T]):

    def __init__(self, elements: list[list[T]] | list[T]) -> None:
        self_elements = []
        if isinstance(elements[0], list):
            for i in range(len(elements)):
                self_elements.append(elements[i].copy())
        else:
            self_elements = [[element] for element in elements]
        self.elements = self_elements
        self.rows = len(self_elements)
        self.cols = len(self_elements[0])

    def check_sizes(self, other: 'Matrix[T]') -> None:
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f'Невозможно выполнить операцию между матрицами размеров '
                f'{self.rows}x{self.cols} и {other.rows}x{other.cols}'
            )

    def __add__(self, other: 'Matrix[T]') -> 'Matrix[T]':
        self.check_sizes(other)
        sum_elements = []
        for i in range(self.rows):
            sum_elements.append([])
            for j in range(self.cols):
                sum_elements[i].append(self.elements[i][j] + other.elements[i][j])
        return Matrix(sum_elements)

    def __sub__(self, other: 'Matrix[T]') -> 'Matrix[T]':
        self.check_sizes(other)
        sub_elements = []
        for i in range(self.rows):
            sub_elements.append([])
            for j in range(self.cols):
                sub_elements[i].append(self.elements[i][j] - other.elements[i][j])
        return Matrix(sub_elements)

    def __mul__(self, other: 'Matrix[T]') -> 'Matrix[T]':
        if self.cols != other.rows:
            raise ValueError(
                'Невозможно выполнить операцию умножения матриц с размерами '
                f'{self.rows}x{self.cols} и {other.rows}x{other.cols}'
            )
        mul_elements = []
        for i in range(self.rows):
            mul_row = []
            for j in range(other.cols):
                mul_element = self.elements[i][j].get_zero()
                for k in range(self.cols):
                    mul_element = mul_element + self.elements[i][k] * other.elements[k][j]
                mul_row.append(mul_element)
            mul_elements.append(mul_row)

        return Matrix(mul_elements)

    def __str__(self) -> str:
        return '\n'.join((f"{str(self.elements[i])}" for i in range(len(self.elements))))

    def __repr__(self) -> str:
        return self.__str__()
