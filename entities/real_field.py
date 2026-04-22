from entities.base import MathField


class R(MathField):

    def __init__(self, value: float) -> None:
        self.value = value

    def __add__(self, other: 'R') -> 'R':
        return R(self.value + other.value)

    def __sub__(self, other: 'R') -> 'R':
        return R(self.value - other.value)

    def __mul__(self, other: 'R') -> 'R':
        return R(self.value * other.value)

    def __truediv__(self, other: 'R') -> 'R':
        return R(self.value / other.value)

    def __pow__(self, power: int) -> 'R':
        return R(pow(self.value, power))

    def inverse(self) -> 'R':
        return R(1 / self.value)

    def __eq__(self, other: 'R') -> bool:
        return self.value == other.value

    def __ne__(self, other: 'R') -> bool:
        return self.value != other.value

    def get_zero(self: 'R') -> 'R':
        return R(0)

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)
