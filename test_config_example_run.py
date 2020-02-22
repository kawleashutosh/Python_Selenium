import pytest


def test_config_example(input_value, setup_methods):
    print("values from fixture is {}".format(input_value))
    print("This method shows example for config file")
