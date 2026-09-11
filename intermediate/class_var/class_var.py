"""
TODO:

Class `Foo` has a class variable `bar`, which is an integer.
"""
from typing import ClassVar

class Foo:
    bar: ClassVar[int]
    ...
Foo.bar = 1
Foo.bar = "1"  # expect-type-error
Foo().bar = 1  # expect-type-error