import allure
from api_clients.base_api import BaseApi


class GetIds(BaseApi):

    def __init__(self, session):
        self.session = session

    @allure.step("Get Team ID")
    def get_team_id(self):
        self.response = self.session.get(
            url="https://api.clickup.com/api/v2/team",
        )
        self.response.raise_for_status()
        self.response_json = self.response.json()
        return self.response_json["teams"][0]["id"]

    @allure.step("Get Space ID for team_id")
    def get_space_id(self, team_id):
        self.response = self.session.get(
            url=f"https://api.clickup.com/api/v2/team/{team_id}/space",
        )
        self.response.raise_for_status()
        self.response_json = self.response.json()
        return self.response_json["spaces"][0]["id"]

    @allure.step("Get Folder ID for space_id")
    def get_folder_id(self, space_id):
        self.response = self.session.get(
            url=f"https://api.clickup.com/api/v2/space/{space_id}/folder",
        )
        self.response.raise_for_status()
        self.response_json = self.response.json()
        return self.response_json["folders"][0]["id"]

    @allure.step("Get List ID for folder_id")
    def get_list_id(self, folder_id):
        self.response = self.session.get(
            url=f"https://api.clickup.com/api/v2/folder/{folder_id}/list",
        )
        self.response.raise_for_status()
        self.response_json = self.response.json()
        return self.response_json["lists"][0]["id"]
