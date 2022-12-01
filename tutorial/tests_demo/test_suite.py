import unittest

from tests_demo.test_case import TestDemo


def get_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestDemo)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_suite())
