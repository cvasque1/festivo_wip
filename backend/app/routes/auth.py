from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse
from app.config.settings import settings
import urllib.parse


router = APIRouter(prefix="/auth", tags=["auth"])

# Spotify OAuth endpoints
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"

# 1) Request authorization to access data
@router.get("/login")
def login():
    params = {
        "client_id": settings.SPOTIFY_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
        "state": "random_string",
        "scope": "user-read-email user-read-private user-top-read"
    }
    auth_url = f"{SPOTIFY_AUTH_URL}?{urllib.parse.urlencode(params)}"

    print(f"{auth_url}")

    return RedirectResponse(auth_url)
