from typing import Generic, TypeVar, Sequence

from entities.base import MathField

T = TypeVar('T', bound=MathField)

class Polynomial(Generic[T]):

    coefficients: list[T]

    def __init__(self, coefficients: list[T]) -> None:
        self.coefficients = coefficients.copy()

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
        product = [self.coefficients[0].get_zero()] * (len(self.coefficients) - 1 + len(other.coefficients))

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                element_production = self.coefficients[i] * other.coefficients[j]
                if product[i + j] is None:
                    product[i + j] = element_production
                else:
                    product[i + j] += element_production

        result = Polynomial(product)
        result.remove_leading_zeros()
        return result

    def __truediv__(self, other: 'Polynomial[T]') -> 'Polynomial[T]':
        raise NotImplementedError

    def scale(self, other: T) -> 'Polynomial[T]':
        return Polynomial([c * other for c in self.coefficients])

    def __eq__(self, other: object) -> bool:
        if type(other) is not Polynomial:
            raise NotImplementedError

        if len(self.coefficients) != len(other.coefficients):
            return False

        for i in range(len(self.coefficients)):
            if self.coefficients[i] != other.coefficients[i]:
                return False
        return True

    def __ne__(self, other: object) -> bool:
        if type(other) is not Polynomial:
            raise NotImplementedError

        if len(self.coefficients) != len(other.coefficients):
            return False

        for i in range(len(self.coefficients)):
            if self.coefficients[i] != other.coefficients[i]:
                return True
        return False

    def evaluate(self, x: T) -> T:
        result = self.coefficients[0].get_zero()

        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * (x ** i)
        return result

    def remove_leading_zeros(self) -> None:
        zero = self.coefficients[0].get_zero()
        while len(self.coefficients) > 0 and self.coefficients[-1] == zero:
            self.coefficients.pop()
        return None

    def __str__(self) -> str:
        return f'[{", ".join(str(coef) for coef in self.coefficients)}]'

    def __repr__(self) -> str:
        return self.__str__()
