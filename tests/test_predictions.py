import pytest


VALID_PAYLOAD = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
}


def test_prediction_returns_setosa(client):
    """Valid measurements should produce a species."""

    response = client.post("/predict", json=VALID_PAYLOAD)

    assert response.status_code == 200
    assert response.json() == {"species": "setosa"}


@pytest.mark.parametrize(
    "payload, expected_error",
    [
        (
            {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
            },
            "missing",
        ),
        (
            {**VALID_PAYLOAD, "flower_height": 8.0},
            "extra_forbidden",
        ),
        (
            {**VALID_PAYLOAD, "sepal_length": "wrong"},
            "float_type",
        ),
        (
            {**VALID_PAYLOAD, "petal_width": -0.2},
            "greater_than",
        ),
    ],
)
def test_invalid_prediction_returns_422(
    client,
    payload,
    expected_error,
):
    """Invalid measurements should fail validation."""

    response = client.post("/predict", json=payload)

    assert response.status_code == 422

    errors = response.json()["detail"]
    assert any(
        error["type"] == expected_error
        for error in errors
    )
