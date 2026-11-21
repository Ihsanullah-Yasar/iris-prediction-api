from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field


FlowerMeasurement = Annotated[
    float,
    Field(
        gt=0,
        allow_inf_nan=False,
        strict=True,
    ),
]


class PredictionRequest(BaseModel):
    """Validate the four Iris flower measurements."""

    model_config = ConfigDict(extra="forbid")

    sepal_length: FlowerMeasurement
    sepal_width: FlowerMeasurement
    petal_length: FlowerMeasurement
    petal_width: FlowerMeasurement


class PredictionResponse(BaseModel):
    """Define the successful prediction response."""

    species: Literal[
        "setosa",
        "versicolor",
        "virginica",
    ]
