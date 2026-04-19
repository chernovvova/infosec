import pytest


@pytest.mark.parametrize(
    ['self', 'other', 'expected'],
    (
        ()
    )
)
def test_polinomyal_add(self, other, expected):
    assert self + other == expected