import pytest


@pytest.mark.django_db
def test_upload_system(client):
    response = client.post('/upload_system/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_votes_for_day(client):
    response = client.get('/votes_for_day/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_vote(client):
    response = client.post('/vote/Penalti/')

    assert response.status_code == 200
