import pytest

from entities.finite_field import Zp


@pytest.mark.parametrize(
    ['a', 'b', 'expected'],
    (
        (Zp(1, 5), Zp(3, 5), Zp(4, 5)),
    ),
)
def test_zp_add(a, b, expected):
    assert a + b == expected