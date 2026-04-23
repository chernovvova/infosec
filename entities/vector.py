from typing import TypeVar, Generic

from entities.base import MathField

T = TypeVar('T', bound=MathField)

class Vector(Generic[T]):

    def __init__(self, coordinates: list[T]) -> None:
        self.coordinates = coordinates.copy()

    def __str__(self) -> str:
        return str(self.coordinates)

    def __repr__(self) -> str:
        return str(self.coordinates)