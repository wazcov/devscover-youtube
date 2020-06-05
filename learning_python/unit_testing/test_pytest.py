import pymain
import pytest

def test_doubleme():
    assert pymain.doubleme(2) == 4

# To Run: pytest