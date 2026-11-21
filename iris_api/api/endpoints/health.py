from fastapi import APIRouter, HTTPException, Request, status


router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check(request: Request) -> dict[str, str]:
    """Report whether the prediction model is ready."""

    model = getattr(request.app.state, "model", None)

    if model is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Prediction model is not ready",
        )

    return {"status": "healthy"}
