import pytest
@pytest.mark.login
def test_m1():
    str = "pretty"
    assert str.upper() == "PRETTY"
    print (str.upper())


def test_m2():
    a=7
    b=8
    assert a+1==b
    print(a+1)

@pytest.mark.login
def test_m3():
    a=682456
    to_array = [char for char in str(a)]
    print(to_array)
    print(len(to_array))







