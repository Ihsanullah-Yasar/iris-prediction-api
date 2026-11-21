from fastapi import HTTPException, Request, status
from sklearn.tree import DecisionTreeClassifier


def get_model(request: Request) -> DecisionTreeClassifier:
    """Return the trained classifier or report unavailability."""

    model = getattr(request.app.state, "model", None)

    if model is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Prediction model is not ready",
        )

    return model
