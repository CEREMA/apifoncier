"""Configuration globale pour les tests pytest."""

import pytest
from unittest.mock import Mock


@pytest.fixture(scope="session")
def mock_client_session():
    """Client mock partagé pour toute la session de tests."""
    client = Mock()
    client.config.base_url = "https://datafoncier.cerema.fr/api"
    return client


@pytest.fixture
def sample_valid_codes_insee():
    """Codes INSEE valides pour les tests."""
    return ["59350", "59100", "62041", "80021"]


@pytest.fixture
def sample_valid_bbox():
    """Bounding box valide pour les tests."""
    return [3.0, 50.6, 3.5, 51.0]


@pytest.fixture
def sample_geojson_point():
    """Point GeoJSON pour les tests."""
    return {"type": "Point", "coordinates": [3.0632, 50.6292]}
