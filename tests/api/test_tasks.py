import allure
import pytest


@allure.step("Test create task")
def test_create_task(task_api_endpoints, clickup_ids):
    list_id = clickup_ids["list_id"]
    name = "Test Task"
    description = "Test task description"
    task_api_endpoints.create_task(list_id, name, description)
    task_id = task_api_endpoints.response_json["id"]
    yield task_id

    assert task_api_endpoints.response.status_code == 200
    task_api_endpoints.assert_status_code_is(200)
    task_api_endpoints.assert_response_field("name", name)
    task_api_endpoints.assert_response_field("description", description)
    task_api_endpoints.delete_task(task_id)


@allure.step("Test get task")
def test_get_task(task_api_endpoints, new_task_dy_id):
    task_api_endpoints.get_task(new_task_dy_id)
    assert task_api_endpoints.response.status_code == 200
    assert task_api_endpoints.response_json["id"] == new_task_dy_id


@allure.step("Test update task")
def test_update_task_name(new_task_dy_id, task_api_endpoints):
    new_name = 'New task name updated'
    task_api_endpoints.update_task(new_task_dy_id, new_name)

    assert task_api_endpoints.response.status_code == 200
    task_api_endpoints.assert_response_field('name', new_name)
    task_api_endpoints.assert_status_code_is(200)


@allure.step("Test delete task")
def test_delete_task(task_api_endpoints, clickup_ids):
    list_id = clickup_ids["list_id"]
    task_api_endpoints.create_task(list_id, "Task to delete")
    task_id = task_api_endpoints.response_json["id"]

    task_api_endpoints.delete_task(task_id)
    assert task_api_endpoints.response.status_code == 204


@pytest.mark.parametrize("name, description, expected_status", [
    ("", "desc", 400),
    (None, "desc", 400)
])
@allure.step("Test negative create task")
def test_negative_create_task(task_api_endpoints, clickup_ids, name, description, expected_status):
    list_id = clickup_ids["list_id"]
    task_api_endpoints.create_task(list_id, name, description)
    assert task_api_endpoints.response.status_code == expected_status


@allure.step("Test get task with invalid ID")
def test_get_task_invalid(task_api_endpoints):
    task_api_endpoints.get_task("invalid_id")
    assert task_api_endpoints.response.status_code == 401
    assert "err" in task_api_endpoints.response.text.lower()


@allure.step("Test update task with invalid ID")
def test_update_task_invalid(task_api_endpoints):
    task_api_endpoints.update_task("invalid_id", "Name")
    assert task_api_endpoints.response.status_code == 401
    assert "err" in task_api_endpoints.response.text.lower()
