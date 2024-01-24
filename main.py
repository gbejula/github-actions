# This is to test actions

def test(a, e):
    return a * e

def test_multiply():
    assert test_multiply(3, 4) == 12
    assert test_multiply(5, -7) == -35
