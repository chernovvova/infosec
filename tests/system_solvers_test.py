import pytest

from entities.base import MathField
from entities.finite_field import Zp
from entities.system_solvers import SystemSolver


@pytest.mark.parametrize(
    ('a', 'b', 'result'),
    (
        (
            [
                [Zp(1, 7), Zp(2, 7)],
                [Zp(3, 7), Zp(1, 7)],
            ],
            [Zp(3, 7), Zp(2, 7)],
            [Zp(3, 7), Zp(0, 7)]
        ),
    )

)
def test_gauss_method(a: list[list[MathField]], b: list[MathField], result) -> None:
    assert SystemSolver.gauss_method(a, b) == result