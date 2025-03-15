from fastapi.testclient import TestClient
from app.main import app  # Ensure this import path is correct
from unittest.mock import patch, MagicMock
from sqlalchemy.orm import Session


@patch("requests.post")
@patch("requests.get")
@patch("app.services.auth_service.save_or_update_user")  # Mock DB function
def test_auth_callback(mock_save_user, mock_get, mock_post, client):
    """Test that /auth/callback correctly exchanges code for token and retrieves user info."""

    # Step 1: Mock token exchange response
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "access_token": "fake_access_token",
        "refresh_token": "fake_refresh_token",
        "expires_in": 3600
    }

    # Step 2: Mock user info response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "id": "fake_spotify_id",
        "display_name": "Fake User",
        "images": [{"url": "https://example.com/image.jpg"}]
    }

    # Step 3: Mock DB session to prevent real DB writes
    mock_db = MagicMock(spec=Session)

    # Step 4: Simulate a request to /auth/callback
    response = client.get(
        "/auth/callback",
        params={"code": "fake_code", "state": "fake_state"},
        cookies={"auth_state": "fake_state"}  # Simulating stored state cookie
    )

    # Step 5: Assertions
    assert response.status_code == 307  # Redirect to the frontend
    mock_save_user.assert_called_once_with(mock_db, mock_get.return_value.json.return_value, mock_post.return_value.json.return_value)