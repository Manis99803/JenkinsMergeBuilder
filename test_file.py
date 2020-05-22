import unittest
from add.add import add

def test_add():
    value = add(1)
    assert value == 14