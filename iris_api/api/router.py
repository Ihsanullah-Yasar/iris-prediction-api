from fastapi import APIRouter

from iris_api.api.endpoints.health import router as health_router
from iris_api.api.endpoints.predictions import router as prediction_router


api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(prediction_router)
