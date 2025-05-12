import allure
import requests


class BaseApi:
    response: requests.Response
    response_json: dict

    @allure.step("Assert that status code is")
    def assert_status_code_is(self, status_code):
        assert self.response.status_code == status_code, \
            f"Expected status code {status_code}, got {self.response.status_code}"

    @allure.step("Assert that response field")
    def assert_response_field(self, field, expected_value):
        assert self.response_json.get(field) == expected_value, \
            f"Expected '{field}' to be '{expected_value}'"
