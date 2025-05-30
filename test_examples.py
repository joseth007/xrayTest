import pytest

# Necesitarás importar pytest para el marcador
# No necesitas importar 'xray' directamente desde el plugin, solo el marcador

def test_user_login_successful():
    """
    This test verifies that a user can log in successfully.
    Corresponds to Jira Test Case PROJ-123.
    """
    assert True

def test_invalid_password_login_fails():
    """
    This test verifies that login fails with an invalid password.
    Corresponds to Jira Test Case PROJ-124.
    """
    assert False, "Simulating a failed test for PROJ-124"

def test_forgot_password_link_present():
    """
    This test checks if the 'Forgot Password' link is visible.
    Corresponds to Jira Test Case PROJ-125.
    """
    assert 1 + 1 == 2

# Las pruebas sin marcador no se incluirán en el reporte JSON de Xray
# a menos que el plugin tenga una configuración para incluirlas por defecto.
# Es mejor marcar todas las pruebas relevantes.
def test_unmapped_example():
    assert True
