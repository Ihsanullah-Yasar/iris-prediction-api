import pytest
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

from app import app


def test_model_is_initialized(client):
    """Verify the application initialized the expected classifier."""

    model = app.state.model

    assert isinstance(model, DecisionTreeClassifier)
    assert model.n_features_in_ == 4
    assert model.classes_.tolist() == [0, 1, 2]


@pytest.mark.parametrize("sample_index", [0, 50, 100])
def test_model_predicts_reference_samples(client, sample_index):
    """Verify the classifier predicts known Iris training samples."""

    iris = load_iris()
    model = app.state.model

    features = iris.data[sample_index:sample_index + 1]
    expected_class = int(iris.target[sample_index])

    predicted_class = int(model.predict(features)[0])

    assert predicted_class == expected_class
