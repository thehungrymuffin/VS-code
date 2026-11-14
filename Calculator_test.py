import pytest
from Circuit_Calculator import Solve_DC
from Circuit_Calculator import resistance_series
from Circuit_Calculator import resistance_parallel


def test_voltage_and_resistance():
    V, I, R, P = Solve_DC(12, None, 4, None)
    assert I == pytest.approx(3)
    assert P == pytest.approx(36)


def test_voltage_and_current():
    V, I, R, P = Solve_DC(10, 2, None, None)
    assert R == pytest.approx(5)
    assert P == pytest.approx(20)


def test_current_and_resistance():
    V, I, R, P = Solve_DC(None, 2, 5, None)
    assert V == pytest.approx(10)
    assert P == pytest.approx(20)


def test_voltage_and_power():
    V, I, R, P = Solve_DC(12, None, None, 36)
    assert I == pytest.approx(3)
    assert R == pytest.approx(4)

def test_series():
    assert resistance_series([100, 200, 300]) == pytest.approx(600)

def test_parallel():
    assert resistance_parallel([100, 100]) == pytest.approx(50)

def test_parallel_zero_resistor():
    with pytest.raises(ZeroDivisionError):
        resistance_parallel([100, 0])

def test_series_empty():
    assert resistance_series([]) == 0

def test_parallel_empty():
    with pytest.raises(ValueError):
        resistance_parallel([])