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
    user_input = driver.find_element(By.ID, EMAIL_INPUT)
    user_input.send_keys(user_creds["username"])

    password_input = driver.find_element(By.ID, PASSWORD_INPUT)
    password_input.send_keys(user_creds["password"])

    sign_in_button = driver.find_element(By.CSS_SELECTOR, SIGN_IN_BUTTON)
    sign_in_button.click()

    wait = WebDriverWait(driver, 4)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="sidebar-estate-plans"]/span')))


@pytest.mark.parametrize(
    "username,password,expected_error",
    INVALID_CREDS.values(),
    ids=INVALID_CREDS.keys()
)
def test_invalid_login(driver, username, password, expected_error):
    user_input = driver.find_element(By.ID, EMAIL_INPUT)
    user_input.send_keys(username)

    password_input = driver.find_element(By.ID, PASSWORD_INPUT)
    password_input.send_keys(password)

    sign_in_button = driver.find_element(By.CSS_SELECTOR, SIGN_IN_BUTTON)
    sign_in_button.click()

    wait = WebDriverWait(driver, 4)

    if "message" in expected_error:
        global_message_el = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, GLOBAL_ERROR_MESSAGE_CLASS)))
        global_description_el = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, GLOBAL_ERROR_DESCRIPTION_CLASS)))
        assert expected_error["message"] in global_message_el.text
        assert expected_error["description"] in global_description_el.text

    if "username" in expected_error:
        username_error_el = wait.until(ec.visibility_of_element_located((By.ID, EMAIL_ERROR_ID)))
        assert expected_error["username"] in username_error_el.text

    if "password" in expected_error:
        password_error_el = wait.until(ec.visibility_of_element_located((By.ID, PASSWORD_ERROR_ID)))
        assert expected_error["password"] in password_error_el.text
