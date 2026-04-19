from typing import Generic, TypeVar, Sequence

from entities.base import BaseMathEntity

T = TypeVar('T', bound=BaseMathEntity)

class Polynomial(BaseMathEntity, Generic[T]):

    def __init__(self, coefficients: list[T | None]) -> None:
        if any(elem is None for elem in coefficients):
            raise ValueError('Коэффициенты не могут быть None')
        self.coefficients = coefficients

    def __add__(self, other: 'Polynomial[T]') -> 'Polynomial[T]':
        a = self.coefficients.copy()
        b = other.coefficients.copy()

        if len(a) > len(b):
            a, b = b, a

        for i in range(len(a)):
            b[i] += a[i]

        result = Polynomial(coefficients=b)
        result.remove_leading_zeros()
        return result

    def __sub__(self, other: 'Polynomial[T]') -> 'Polynomial[T]':
        a = self.coefficients.copy()
        b = other.coefficients.copy()

        if len(a) < len(b):
            a, b = b, a

        for i in range(len(a)):
            a[i] -= b[i]

        result = Polynomial(coefficients=a)
        result.remove_leading_zeros()
        return result

    def __mul__(self, other: 'Polynomial[T]') -> 'Polynomial[T]':
        product = [None] * (len(self.coefficients) - 1 + len(other.coefficients))

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                element_production = self.coefficients[i] * other.coefficients[j]
                if product[i + j] is None:
                    product[i + j] = element_production
                else:
                    product[i + j] += element_production

        result = Polynomial(coefficients=product)
        result.remove_leading_zeros()
        return result

    def scale(self, other: T) -> 'Polynomial[T]':
        return Polynomial([c * other for c in self.coefficients])


    def __eq__(self, other: 'Polynomial[T]') -> bool:
        if len(self.coefficients) != len(other.coefficients):
            return False

        for i in range(len(self.coefficients)):
            if self.coefficients[i] != other.coefficients[i]:
                return False
        return True

    def evaluate(self, x: T) -> T:
        result = None

        for i in range(len(self.coefficients)):
            if result is None:
                result = self.coefficients[i] * (x ** i)
            else:
                result += self.coefficients[i] * (x ** i)
        return result

    def remove_leading_zeros(self) -> None:
        zero = type(self.coefficients[0]).zero(p=self.coefficients[0].p)
        while len(self.coefficients) > 0 and self.coefficients[-1] == zero:
            self.coefficients.pop()
        return None

    def __str__(self) -> str:
        return f'[{", ".join(str(coef) for coef in self.coefficients)}]'