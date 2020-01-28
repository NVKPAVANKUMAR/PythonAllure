import pytest


@pytest.mark.flaky(reruns=5)
def test_example():
    assert True
