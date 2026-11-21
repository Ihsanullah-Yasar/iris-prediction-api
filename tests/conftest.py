import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture
def client():
    """Provide a test client with application lifespan enabled."""

    with TestClient(app) as test_client:
        yield test_client
