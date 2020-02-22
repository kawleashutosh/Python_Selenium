import pytest


# setting fixture that  return values to test methods
@pytest.fixture()
def input_val():
    inpt = 39
    return inpt


# fixture example that will run at start and end of each test
@pytest.fixture()
def setup():
    print("This line will execute at start of each test")
    yield
    print("This line will execute at the end of each test")


def test_div_by_3(input_val, setup):
    print(input_val)
    assert input_val % 3 == 0, "Not divisible by 3"


def test_div_by_6(input_val, setup):
    print(input_val)
    assert input_val % 6 == 0, "Not divisible by 6"

