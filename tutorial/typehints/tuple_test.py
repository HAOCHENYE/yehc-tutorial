from typing import Tuple


def foo(x: Tuple[int, ...]) -> Tuple[int, ...]:
    return x


foo((1, 1.0))
