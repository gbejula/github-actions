# This is to test actions

def test(a, e):
    return a * e

def test_multiply():
    assert test(3, 4) == 12
    assert test(5, 7) == 35
