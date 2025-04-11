from app import add
from app import sub

def test_add():
    assert add(2,3) == 5
    assert add(4,3) == 7

def test_sub():
    assert sub(3,1) == 2
    assert sub(5,4) == 1