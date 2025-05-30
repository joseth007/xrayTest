import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def test_user_login_successful(record_property):
    record_property("test_key", "CT-1252")
    """
    This test verifies that a user can log in successfully.
    """
    assert True

def test_invalid_password_login_fails(record_property):
    record_property("test_key", "CT-1315")
    """
    This test verifies that login fails with an invalid password.
    """
    assert False, "Simulating a failed test for PROJ-124"

def test_forgot_password_link_present(record_property):
    record_property("test_key", "CT-1311")
    """
    This test checks if the 'Forgot Password' link is visible.
    """
    assert 1 + 1 == 2

def test_unmapped_example(record_property):
    assert True


def test_successful_login_saucedemo(record_property):
    record_property("test_key", "CT-3283")
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url
    allure.attach(driver.get_screenshot_as_png(), name="login_success_screenshot", attachment_type=allure.attachment_type.PNG)

    driver.quit()


def test_failed_login_saucedemo(record_property):
    record_property("test_key", "CT-3284")
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

        # Wait for error message to be present
    error_message_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    )
    assert "Epic sadface: Sorry, this user has been locked out." in error_message_element.text
    allure.attach(driver.get_screenshot_as_png(), name="login_failure_screenshot", attachment_type=allure.attachment_type.PNG)
    driver.quit()
