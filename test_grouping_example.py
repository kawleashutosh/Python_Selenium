import pytest

''' This file shows how to group test in pytest'''

@pytest.mark.grpone
def group_one_example_1():
    print("This example {} is from group {}".format(1, "one"))


@pytest.mark.grpone
def test_group_one_example_2():
    print("This example {} is from group {}".format(2, "one"))


@pytest.mark.grptwo
def test_group_two_example_1():
    print("This example {} is from group {}".format(1, 'two'))


@pytest.mark.grptwo
def test_group_two_example_2():
    print("This example {} is from group {}".format(2, 'two'))
