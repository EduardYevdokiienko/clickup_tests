import allure
import requests
from constant import BASE_URL, HEADERS
from api_clients.base_api import BaseApi


class AuthApi(BaseApi):

    @allure.step("Initialize AuthApi and create session")
    def __init__(self):
        self.headers = HEADERS
        self.session = self.create_session()

    @allure.step("Create and configure HTTP session")
    def create_session(self):
        session = requests.Session()
        session.headers.update(self.headers)
        return session

    @allure.step("Get current HTTP session")
    def get_session(self):
        return self.session

    @allure.step("Request authorized user information")
    def get_authorized_user_info(self):
        self.response = self.session.get(f"{BASE_URL}/user")
        self.response_json = self.response.json()
