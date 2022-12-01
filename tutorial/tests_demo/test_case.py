from unittest import TestCase


def add(a, b):
    return a + b


def minors(a, b):
    return a - b


class TestDemo(TestCase):
    def setUp(self) -> None:
        print("setup test")

    @classmethod
    def tearDown(cls) -> None:
        print("teardown test")

    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    def tearDownClass() -> None:
        print("teardown class")

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_minors(self):
        self.assertEqual(minors(1, 2), -1)
