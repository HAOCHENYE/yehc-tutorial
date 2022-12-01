from unittest import TestCase


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

