# Iris Prediction API

A containerized Machine Learning REST API built with FastAPI, scikit-learn, and Docker for a Cloud Computing practical assignment.

## Overview

The API uses a DecisionTreeClassifier trained on scikit-learn's built-in Iris dataset to predict flower species from four measurements.

The classifier is trained once during application startup and reused for prediction requests.

## Technology Stack

- Python 3.11 (Docker image)
- FastAPI and Uvicorn
- Pydantic
- scikit-learn
- pytest
- Docker

## API Endpoints

### GET /health

Checks whether the trained model is available.

Successful response (200):

```json
{ "status": "healthy" }
```

Returns HTTP 503 if the model is not ready.

### POST /predict

Request:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Successful response (200):

```json
{ "species": "setosa" }
```

Supported species: setosa, versicolor, virginica.

Invalid requests return HTTP 422.

## Local Development

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Windows Git Bash:

```bash
source .venv/Scripts/activate
```

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run the API:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Swagger UI:

http://localhost:8000/docs

## Run with Docker

Build the image:

```bash
docker build -t iris-ai:v1 .
```

Create and start the container:

```bash
docker run -d --name iris-api -p 8000:8000 iris-ai:v1
```

Verify the container:

```bash
docker ps
docker logs iris-api
```

Monitor resource usage:

```bash
docker stats --no-stream iris-api
```

Stop and restart:

```bash
docker stop iris-api
docker start iris-api
```

## Automated Testing

Run the test suite:

```bash
python -m pytest -v
```

Verified result: 10 tests passed.

The tests cover API health, model initialization, sample predictions, and invalid request handling.

Tests using training samples confirm basic functionality, not generalization performance on unseen data.

## Architecture

- `app.py`: Application entry point and model training lifecycle
- `iris_api/main.py`: FastAPI application factory
- `iris_api/api/`: Endpoints, router, and dependencies
- `iris_api/schemas/`: Request and response validation
- `iris_api/services/`: Prediction business logic
- `iris_api/ml/`: Feature preparation
- `tests/`: Automated tests
- `Dockerfile`: Container image definition

## Notes

The model is trained in memory during startup. No external database or saved model file is required.

This project is intended for educational demonstration.

## Team and Acknowledgments

Add the actual team members, their responsibilities, and any AI assistance or external resources used.
