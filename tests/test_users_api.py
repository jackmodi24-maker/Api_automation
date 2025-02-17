import pytest
from utils.api_client import APIClient
import uuid

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_users(api_client,load_user_data):
    # user_data = {
    #     "name": "prasanth",
    #     "username":"qa user",
    #     "email":"test@gmail.com"
    # }
#hi hello prasanth
    user_data = load_user_data["new_user"]

    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"] = unique_email

    response = api_client.post("users", user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == 'prasanth'
    id = response.json()['id']
    responseget = api_client.get("users/10")
    print(responseget.json())
    assert responseget.status_code == 200
    assert responseget.json()['name'] == 'Clementina DuBuque'


def test_update_users(api_client):
    user_data = {
        "name": "David Greg",
        "username":"David",
        "email":"david@gmail.com"
    }
    response = api_client.put("users/1", user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == 'David'


def test_delete_users(api_client):
    response = api_client.delete("users/1")
    print(response.json())
    assert response.status_code == 200
