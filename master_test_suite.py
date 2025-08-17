import pytest

if __name__ == "__main__":
    test_suites = {
        "functional_tests": "tests/functional_tests",
        "integration_tests": "tests/integration_tests",
        "e2e_tests": "tests/e2e_tests"
    }

    suite_to_run = test_suites["e2e_tests"]

    pytest.main([suite_to_run])
