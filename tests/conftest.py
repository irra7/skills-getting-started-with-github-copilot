import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as original_activities


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    saved_state = copy.deepcopy(original_activities)
    yield
    original_activities.clear()
    original_activities.update(saved_state)
