from collections.abc import Callable
from contextlib import AbstractAsyncContextManager

from fastapi import FastAPI

from iris_api.api.router import api_router


def create_app(
    *,
    lifespan: Callable[
        [FastAPI], AbstractAsyncContextManager[None]
    ] | None = None,
) -> FastAPI:
    """Create and configure the FastAPI application."""

    application = FastAPI(
        title="Iris Prediction API",
        description="Containerized Iris flower classification API",
        version="0.1.0",
        lifespan=lifespan,
    )

    application.include_router(api_router)

    return application
