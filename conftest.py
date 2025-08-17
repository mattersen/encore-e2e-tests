import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(os.getenv("QA_ENV"))
    yield driver
    driver.quit()

@pytest.fixture
def user_creds(request):
    return request.getfixturevalue(request.param)

@pytest.fixture
def admin_user_creds():
    return {"username": os.getenv("ADMIN_USERNAME"), 'password': os.getenv("ADMIN_PASSWORD")}

@pytest.fixture
def advisor_user_creds():
    return {"username": os.getenv("ADVISOR_USERNAME"), 'password': os.getenv("ADVISOR_PASSWORD")}

@pytest.fixture
def client_user_creds():
    return {"username": os.getenv("CLIENT_USERNAME"), 'password': os.getenv("CLIENT_PASSWORD")}

@pytest.fixture
def guest_user_creds():
    return {"username": os.getenv("GUEST_USERNAME"), 'password': os.getenv("GUEST_PASSWORD")}
