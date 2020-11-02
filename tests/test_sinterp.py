import pytest

from sinterp.sinterp import interp1d


def test_interp1d_1():
    x = 0.5
    y1 = x1 = 0.0
    y2 = x2 = 1.0
    value = interp1d(x, [x1, x2], [y1, y2])
    assert value == y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)


def test_interp1d_2():
    with pytest.raises(ValueError):
        x = -1.0
        y1 = x1 = 0.0
        y2 = x2 = 1.0
        interp1d(x, [x1, x2], [y1, y2])


def test_interp1d_3():
    with pytest.raises(ValueError):
        x = 2.0
        y1 = x1 = 0.0
        y2 = x2 = 1.0
        interp1d(x, [x1, x2], [y1, y2])


def test_interp1d_4():
    with pytest.raises(ValueError):
        x = 2.0
        y1 = x1 = 0.0
        y2 = 1.0
        interp1d(x, [x1], [y1, y2])


def test_interp1d_5():
    with pytest.raises(ValueError):
        x = 2.0
        x1 = 0.0
        y2 = x2 = 1.0
        interp1d(x, [x1, x2], [y2])


def test_interp1d_6():
    with pytest.raises(ValueError):
        x = 2.0
        y1 = x1 = 0.0
        y2 = x2 = 1.0
        x3 = 2.0
        interp1d(x, [x1, x2, x3], [y1, y2])
