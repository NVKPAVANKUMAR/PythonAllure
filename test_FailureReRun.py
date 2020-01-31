import pytest


@pytest.mark.flaky(reruns=5)
def test_example():
    assert True


@pytest.mark.xfail(raises=ArithmeticError)
def test_01():
    print(10 / 0)


@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num > 100


@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.xfail
@pytest.mark.others
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.skip
def test_less():
    num = 100
    assert num < 200


# Pytest - Stop Test Suite after N Test Failures
import math


def test_sqrt_failure():
    num = 25
    assert math.sqrt(num) == 6


def test_square_failure():
    num = 7
    assert num * num == 40


def test_equality_failure():
    assert 10 == 11
