from collections.abc import Mapping


FEATURE_ORDER = (
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
)


def build_feature_matrix(
    measurements: Mapping[str, float],
) -> list[list[float]]:
    """Prepare one Iris sample for model inference."""

    return [
        [measurements[name] for name in FEATURE_ORDER]
    ]
