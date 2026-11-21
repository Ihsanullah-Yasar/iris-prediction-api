from typing import Annotated

from fastapi import APIRouter, Depends
from sklearn.tree import DecisionTreeClassifier

from iris_api.api.dependencies import get_model
from iris_api.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
)
from iris_api.services.prediction_service import predict_species


router = APIRouter(tags=["Predictions"])


@router.post("/predict", response_model=PredictionResponse)
def predict(
    request: PredictionRequest,
    model: Annotated[
        DecisionTreeClassifier,
        Depends(get_model),
    ],
) -> PredictionResponse:
    """Predict the species of an Iris flower."""

    return predict_species(model, request)
