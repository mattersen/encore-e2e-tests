# Encore E2E Tests

A Python + Selenium end-to-end test suite for Encore Estate Plans.

---

##  What & Why

This repository contains a variety of different E2E workflows including:
1. User Authentication - Test automation suite for verifying Encore user authentication flows. It helps ensure login with a variety of different user profiles is working reliably.
2. More to come...

##  Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/mattersen/encore-e2e-tests.git
   cd encore-e2e-tests
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
How to Run
  - To run full suite:
    ```bash
    pytest -v
  - To run single test:
    ```bash
    pytest tests/test_login.py

Key Features
- End-to-end testing of login workflow with a variety of user profiles.
- Built using **Python**, **Selenium**, and **pytest**
- Extendable for additional auth scenarios

##  Author
Matthew Andersen
