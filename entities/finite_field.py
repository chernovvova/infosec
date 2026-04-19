from entities.base import BaseMathEntity
from utils import mod_inverse, quick_pow


class Zp(BaseMathEntity):

    def __init__(self, value: int, p: int) -> None:
        self.value = value % p
        self.p = p

    def check_p(self, other: 'Zp') -> bool:
        return self.p == other.p

    def __add__(self, other: 'Zp') -> 'Zp':
        return Zp((self.value + other.value) % self.p, self.p)

    def __sub__(self, other: 'Zp') -> 'Zp':
        return Zp((self.value - other.value) % self.p, self.p)

    def __mul__(self, other: 'Zp') -> 'Zp':
        return Zp((self.value * other.value) % self.p, self.p)

    def __truediv__(self, other: 'Zp') -> 'Zp':
        return self * other.inverse()

    def __pow__(self, power: int) -> 'Zp':
        return Zp(quick_pow(self.value, power, self.p), self.p)

    def inverse(self) -> 'Zp':
        return Zp(mod_inverse(self.value, self.p), self.p)

    def __eq__(self, other: 'Zp') -> bool:
        return self.check_p(other) and self.value == other.value

    @staticmethod
    def zero(p: int = 1) -> 'Zp':
        return Zp(0, p)

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)