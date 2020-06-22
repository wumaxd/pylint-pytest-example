import pytest


def test_with_local_fixture(local_fixture):
    """
    Fixtures can be invoked simply by having a positional arg
    with the same name as a fixture:
    """
    print("Running test_with_local_fixture...")
    assert True


@pytest.fixture
def local_fixture():
    """
    Fixtures are callables decorated with @fixture
    """
    print("\n(Doing Local Fixture setup stuff!)")
