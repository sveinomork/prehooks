# tests/test_main.py

from prehooks.main import add


def test_add():
    assert add(2, 3) == 5  # This should pass if add is implemented correctly
