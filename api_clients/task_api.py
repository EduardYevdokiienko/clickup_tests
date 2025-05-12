import requests
import allure
from constant import BASE_URL
from api_clients.base_api import BaseApi


class TasksApi(BaseApi):
    def __init__(self, session: requests.Session):
        super().__init__()
        self.session = session

    @allure.step("Create task in list_id")
    def create_task(self, list_id, name, description=None):
        payload = {
            "name": name,
            "description": description or "Autotest-created task"
        }
        self.response = self.session.post(
            url=f"{BASE_URL}/list/{list_id}/task",
            json=payload
        )
        self.response_json = self.response.json()

    @allure.step("Get task by task_id")
    def get_task(self, task_id):
        self.response = self.session.get(
            url=f"{BASE_URL}/task/{task_id}"
        )
        self.response_json = self.response.json()

    @allure.step("Update task_id")
    def update_task(self, task_id, new_name):
        payload = {
            "name": new_name
        }
        self.response = self.session.put(
            url=f"{BASE_URL}/task/{task_id}",
            json=payload
        )
        self.response_json = self.response.json()

    @allure.step("Delete task by task_id")
    def delete_task(self, task_id):
        self.response = self.session.delete(
            url=f"{BASE_URL}/task/{task_id}"
        )
        if self.response.status_code != 204:
            raise Exception(
                f"Failed to delete task. Status: {self.response.status_code}, Body: {self.response.text}"
            )
