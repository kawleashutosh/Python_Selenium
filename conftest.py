import pytest

''' This will contain group of fixture that would be used across multiple test in project '''


@pytest.fixture()
def input_value():
    return 39


@pytest.fixture()
def setup_methods():
    print("This line should print at start of test")
    yield
    print("This line should print at end of test")
