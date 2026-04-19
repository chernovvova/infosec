import pytest

from entities.finite_field import Zp


@pytest.mark.parametrize(
    ['a', 'b', 'expected'],
    (
        (Zp(1, 5), Zp(1, 5), True),
        (Zp(2, 5), Zp(3, 5), False),
        (Zp(1, 3), Zp(1, 4), False),
    ),
)
def test_zp_eq(a: Zp, b: Zp, expected: Zp) -> None:
    assert bool(a == b) == expected


@pytest.mark.parametrize(
    ['a', 'b', 'expected'],
    (
        (Zp(1, 5), Zp(3, 5), Zp(4, 5)),
        (Zp(2, 5), Zp(3, 5), Zp(0, 5)),
    ),
)
def test_zp_add(a: Zp, b: Zp, expected: Zp) -> None:
    assert (a + b) == expected


@pytest.mark.parametrize(
    ['a', 'b', 'expected'],
    (
        (Zp(4, 5), Zp(3, 5), Zp(1, 5)),
        (Zp(-1, 5), Zp(4, 5), Zp(0, 5)),
    ),
)
def test_zp_sub(a: Zp, b: Zp, expected: Zp) -> None:
    assert (a - b) == expected


@pytest.mark.parametrize(
    ['a', 'b', 'expected'],
    (
        (Zp(4, 5), Zp(3, 5), Zp(2, 5)),
        (Zp(-8, 5), Zp(4, 5), Zp(3, 5)),
    ),
)
def test_zp_sub(a: Zp, b: Zp, expected: Zp) -> None:
    assert (a * b) == expected