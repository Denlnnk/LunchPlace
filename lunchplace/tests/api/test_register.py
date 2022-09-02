import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django.db
def test_register_employee():
    payload = {
        "username": "Antony",
        "email": "anton@gmail.com",
        "password": "admin",
        "first_name": "Anton",
        "last_name": "Kozlov"
    }

    response = client.post('/register/', payload)

    data = response.data

    assert data['username'] == payload['username']
    assert data['email'] == payload['email']
    assert data['password'] == payload['password']
    assert data['first_name'] == payload['first_name']
    assert data['last_name'] == payload['last_name']
