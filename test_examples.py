import pytest

@pytest.mark.xray('CT-1252')
def test_user_login_successful():
    """
    This test verifies that a user can log in successfully.
    """
    assert True

@pytest.mark.xray('CT-1315')
def test_invalid_password_login_fails():
    """
    This test verifies that login fails with an invalid password.
    """
    assert False, "Simulating a failed test for PROJ-124"

@pytest.mark.xray('CT-1311')
def test_forgot_password_link_present():
    """
    This test checks if the 'Forgot Password' link is visible.
    """
    assert 1 + 1 == 2

def test_unmapped_example():
    assert True
