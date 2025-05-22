import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_and_get_records():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Test POST
        payload = {"name": "Test Record", "description": "This is a test record"}
        response = await client.post("/records/", json=payload)
        assert response.status_code == 200
        assert response.json()["name"] == "Test Record"

        # Test GET
        response = await client.get("/records/")
        assert response.status_code == 200
        assert len(response.json()) > 0