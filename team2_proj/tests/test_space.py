import pytest
from team2_proj.team2_proj.POTD import get_potd, validate_date
from unittest.mock import patch
from quart.testing import QuartClient

from team2_proj.team2_proj.space import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    client =  app.test_client()
    yield client


@pytest.mark.asyncio
async def test_index(client):
    response = await client.get('/')
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'

@pytest.mark.asyncio
async def test_POTD(client):
    response = await client.get('/POTD')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    j = await response.json
    assert j["Query"] == "Get More context from Wikipedia."


@pytest.mark.asyncio
async def test_pastPOTD(client):
    response = await client.get('/pastPOTD/2021-11-29')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    j = await response.json
    assert j["Query"] == "Get More context from Wikipedia."


# @pytest.mark.asyncio
# @patch('team2_proj.POTD.validate_date', return_value=False)
# async def test_wrong_date_format(mock_validate_date, client):
#     response = await client.get('/pastPOTD/2021-11-29')
#     response2 = await client.get('/POTD')
#     assert response.status_code == 200
#     j1 = await response.json
#     j2 = await response2.json
#     assert j1 == j2



@pytest.mark.asyncio
async def test_get_wikipedia_data(client):
    response = await client.get('/wikipedia/NASA')
    assert response.status_code == 200
    data = await response.get_json()
    assert 'title' in data

@pytest.mark.asyncio
async def test_get_potd(client):
    response = await client.get('/POTD')
    assert response.status_code == 200
    data = await response.get_json()
    assert 'POTD' in data

@pytest.mark.asyncio
@pytest.mark.parametrize("date, expected_status_code, expected_key", [
    ("2024-04-22", 200, "POTD"),  # Assuming this date exists
    ("InvalidDate", 200, "POTD"),  # Assuming this date does not exist
])
async def test_get_past_potd(client, date, expected_status_code, expected_key):
    response = await client.get(f'/pastPOTD/{date}')
    assert response.status_code == expected_status_code
    data = await response.get_json()
    assert expected_key in data

@pytest.mark.asyncio
async def test_get_potd_due_to_missing_date(client):
    response = await client.get('/pastPOTD')
    assert response.status_code == 200
    data = await response.get_json()
    assert 'POTD' in data

@pytest.mark.asyncio
async def test_index(client):
    response = await client.get('/')
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in await response.get_data()
