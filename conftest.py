import pytest
from api_clients.auth_api import AuthApi
from api_clients.get_ids import GetIds
from api_clients.task_api import TasksApi


@pytest.fixture(scope="session")
def auth_session():
    auth_api = AuthApi()
    return auth_api.get_session()

@pytest.fixture(scope="session")
def new_task_dy_id(auth_session, clickup_ids, task_api_endpoints):
    list_id = clickup_ids["list_id"]
    name = 'test_task'
    description = 'test_task yield del'
    task_api_endpoints.create_task(list_id, name, description)
    task_id = task_api_endpoints.response_json.get('id')
    yield task_id
    task_api_endpoints.delete_task(task_id)


@pytest.fixture(scope="session")
def get_ids(auth_session):
    return GetIds(auth_session)

@pytest.fixture(scope="session")
def clickup_ids(get_ids):
    team_id = get_ids.get_team_id()
    space_id = get_ids.get_space_id(team_id)
    folder_id = get_ids.get_folder_id(space_id)
    list_id = get_ids.get_list_id(folder_id)

    return {
        "team_id": team_id,
        "space_id": space_id,
        "folder_id": folder_id,
        "list_id": list_id
    }

@pytest.fixture(scope='session')
def task_api_endpoints(auth_session):
    return TasksApi(auth_session)
