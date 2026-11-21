def test_health_returns_200_when_ready(client):
    """The health endpoint should indicate readiness."""

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
