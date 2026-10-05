import pytest

from calculator import Calculator


@pytest.mark.parametrize(("left", "right", "expected"), [(2, 3, 5), (-1, 1, 0), (1.5, 2.5, 4)])
def test_add(left, right, expected):
    assert Calculator().add(left, right) == expected


def test_divide():
    assert Calculator().divide(8, 2) == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(1, 0)
