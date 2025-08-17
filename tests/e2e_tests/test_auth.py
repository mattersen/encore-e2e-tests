import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from test_data import INVALID_CREDS
from constants import *

@pytest.mark.parametrize("user_creds", [
    "admin_user_creds",
    "advisor_user_creds",
    "client_user_creds",
    "guest_user_creds"
], ids=["admin", "advisor", "client", "guest"], indirect=True)
def test_valid_login(driver, user_creds):
    user_input = driver.find_element(by=By.ID, value=EMAIL_INPUT)
    user_input.send_keys(user_creds["username"])

    password_input = driver.find_element(by=By.ID, value=PASSWORD_INPUT)
    password_input.send_keys(user_creds["password"])

    sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value=SIGN_IN_BUTTON)
    sign_in_button.click()

    wait = WebDriverWait(driver, 4)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="sidebar-estate-plans"]/span')))


@pytest.mark.parametrize("username,password,expected_error", INVALID_CREDS.values(), ids=INVALID_CREDS.keys())
def test_invalid_login(driver, username, password, expected_error):
    user_input = driver.find_element(by=By.ID, value=EMAIL_INPUT)
    user_input.send_keys(username)

    password_input = driver.find_element(by=By.ID, value=PASSWORD_INPUT)
    password_input.send_keys(password)

    sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value=SIGN_IN_BUTTON)
    sign_in_button.click()

    wait = WebDriverWait(driver, 4)
    error_element = wait.until(ec.visibility_of_element_located((By.ID, 'basic_email_help')))

    assert expected_error == error_element.text
