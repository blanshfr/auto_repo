import pytest

@pytest.fixture(scope="class")
def setup():
    print("It is pre-condition for test_third_pytest")
    yield
    print("It is post-condition for test_third_pytest")
