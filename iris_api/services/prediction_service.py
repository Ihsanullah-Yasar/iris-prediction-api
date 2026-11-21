from sklearn.tree import DecisionTreeClassifier

from iris_api.ml.features import build_feature_matrix
from iris_api.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
)


SPECIES_NAMES = (
    "setosa",
    "versicolor",
    "virginica",
)


def predict_species(
    model: DecisionTreeClassifier,
    request: PredictionRequest,
) -> PredictionResponse:
    """Predict an Iris species using a trained classifier."""

    measurements = request.model_dump()

    features = build_feature_matrix(measurements)

    predicted_class = int(model.predict(features)[0])

    species = SPECIES_NAMES[predicted_class]

    return PredictionResponse(species=species)
