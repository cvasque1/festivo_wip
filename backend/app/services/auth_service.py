# Handle Spotify OAuth logic
from fastapi import APIRouter, Request, Response, HTTPException
from app.config.settings import settings
from app.config.database import get_db
from app.models.user import User
import base64
import requests
import datetime

SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_USER_URL = "https://api.spotify.com/v1/me"

def exchange_code_for_token(code):
    client_creds = f"{settings.SPOTIFY_CLIENT_ID}:{settings.SPOTIFY_CLIENT_SECRET}"
    auth_header = base64.b64encode(client_creds.encode()).decode()

    # Request headers
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Request body
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
    }

    # Send POST request
    response = requests.post(SPOTIFY_TOKEN_URL, data=data, headers=headers)

    # Handle response
    if response.status_code != 200:
        return None, response.json()


    return response.json(), None

    
def get_spotify_user_info(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(SPOTIFY_USER_URL, headers=headers)

    # Handle response
    if response.status_code != 200:
        return None, response.json()

    return response.json(), None


def save_or_update_user(db, user_data, token_data):
    spotify_id = user_data["id"]
    name = user_data["display_name"]
    image_url = user_data.get("images", [{}])[0].get("url", None)
    access_token = token_data["access_token"]
    refresh_token = token_data["refresh_token"]
    expires_in = token_data["expires_in"]

    token_expires_at = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=expires_in)
    user = db.query(User).filter(User.spotify_id == spotify_id).first()

    if user:
        # Update user
        user.access_token = access_token
        user.refresh_token = refresh_token
        user.token_expires_at = token_expires_at
        user.image_url = image_url
    else: 
        # Create user
        new_user = User(
            spotify_id=spotify_id,
            name=name,
            image_url=image_url,
            access_token=access_token,
            refresh_token=refresh_token,
            token_expires_at=token_expires_at
        )
        db.add(new_user)

    db.commit()