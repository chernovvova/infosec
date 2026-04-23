from entities.base import MathField
from utils import mod_inverse, quick_pow


class Zp(MathField):

    def __init__(self, value: int, p: int) -> None:
        self.value = value % p
        self.p = p

    def check_p(self, other: 'Zp') -> None:
        if self.p != other.p:
            raise ValueError('Попытка выполнить операцию между элементами с разным значением p')

    def __add__(self, other: 'Zp') -> 'Zp':
        self.check_p(other)
        return Zp(self.value + other.value, self.p)

    def __sub__(self, other: 'Zp') -> 'Zp':
        self.check_p(other)
        return Zp(self.value - other.value, self.p)

    def __mul__(self, other: 'Zp') -> 'Zp':
        self.check_p(other)
        return Zp(self.value * other.value, self.p)

    def __truediv__(self, other: 'Zp') -> 'Zp':
        self.check_p(other)
        return self * other.inverse()

    def __pow__(self, power: int) -> 'Zp':
        return Zp(quick_pow(self.value, power, self.p), self.p)

    def inverse(self) -> 'Zp':
        return Zp(mod_inverse(self.value, self.p), self.p)

    def __eq__(self, other: object) -> bool:
        if type(self) != type(other):
            raise NotImplementedError
        self.check_p(other)
        return self.value == other.value

    def __ne__(self, other: object) -> bool:
        if type(self) != type(other):
            raise NotImplementedError
        self.check_p(other)
        return self.value != other.value

    def get_zero(self: 'Zp') -> 'Zp':
        return Zp(0, self.p)

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)