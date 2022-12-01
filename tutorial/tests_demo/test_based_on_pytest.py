def add(a, b):
    return a + b


def minors(a, b):
    return a - b


def test_add():
    assert add(1, 2) == 3


def test_minors():
    assert minors(1, 2) == -1
