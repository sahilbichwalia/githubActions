from src.maths_operation import add,sub

def test_add():
    assert add(2,3)==5  ## assert  is used to check whatever output is coming equal or not
    assert add(-1,1)==0


def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
