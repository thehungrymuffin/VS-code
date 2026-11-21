import pytest
from Circuit_Calculator import Solve_DC
from Circuit_Calculator import resistance_series
from Circuit_Calculator import resistance_parallel
from Circuit_Calculator import log_result, read_logs, clear_logs
from CircuitClasses import Resistor


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

def test_log_result_writes_entry(tmp_path):
    f = tmp_path / "history.txt"
    log_result("DC", "test entry", str(f))
    assert "test entry" in f.read_text()

def test_log_result_appends(tmp_path):
    f = tmp_path / "history.txt"
    log_result("DC", "first", str(f))
    log_result("DC", "second", str(f))
    lines = f.read_text().splitlines()
    assert len(lines) == 2

def test_read_logs_missing_file(tmp_path, capsys):
    read_logs(str(tmp_path / "nope.txt"))
    assert "No History" in capsys.readouterr().out

def test_clear_logs(tmp_path):
    f = tmp_path / "history.txt"
    log_result("DC", "entry", str(f))
    clear_logs(str(f))
    assert f.read_text() == ""

def test_valid_resistor():
    assert Resistor(100).resistance == 100

def test_zero_resistance_rejected():
    with pytest.raises(ValueError):
        Resistor(0)

def test_negative_resistance_rejected():
    with pytest.raises(ValueError):
        Resistor(-5)

def test_changing_resistance_is_validated():
    r = Resistor(100)
    with pytest.raises(ValueError):
        r.resistance = -1

def test_current():
    assert Resistor(100).current(12) == pytest.approx(0.12)

def test_power():
    assert Resistor(100).power_output(10) == pytest.approx(1.0)

def test_str():
    assert "100" in str(Resistor(100))