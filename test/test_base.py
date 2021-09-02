from tusk.core import binary_search

def test_exists():
    assert binary_search([3, 4, 5, 6], 4) == 1

def test_not_exists():
    assert binary_search([1, 5, 7, 88], 34) == -1