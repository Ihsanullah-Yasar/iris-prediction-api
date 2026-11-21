from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

from iris_api.main import create_app


@asynccontextmanager
async def lifespan(application: FastAPI) -> AsyncIterator[None]:
    """Train and initialize the classifier during startup."""

    # Load the built-in Iris dataset.
    iris = load_iris()

    # Initialize and train the classifier.
    model = DecisionTreeClassifier(random_state=42)
    model.fit(iris.data, iris.target)

    # Share the trained model across requests.
    application.state.model = model

    try:
        yield
    finally:
        # Release the model reference during shutdown.
        del application.state.model


app = create_app(lifespan=lifespan)
