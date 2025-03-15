from fastapi import APIRouter, Request, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from app.config.settings import settings
from app.services.auth_service import exchange_code_for_token, get_spotify_user_info, save_or_update_user
from app.config.database import get_db
import secrets
import urllib.parse


router = APIRouter(prefix="/auth", tags=["auth"])

FRONTEND_HOME_URL = ""
FRONTEND_APP_URL = ""

# Spotify OAuth endpoints
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"

# 1) Request authorization to access data
@router.get("/login")
def login(response: Response):
    state = secrets.token_urlsafe(16)

    response.set_cookie(key="auth_state", value=state, httponly=True, samesite="lax")

    params = {
        "client_id": settings.SPOTIFY_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
        "state": state,
        "scope": "user-read-email user-read-private user-top-read"
    }
    auth_url = f"{SPOTIFY_AUTH_URL}?{urllib.parse.urlencode(params)}"

    # FastAPI wasn't including the cookie in the redirect so currently using this workaround
    response.status_code = 307
    response.headers["Location"] = auth_url
    return response
    # return RedirectResponse(auth_url)


@router.get("/callback")
def callback(request: Request, db: Session = Depends(get_db)):
    error = request.query_params.get("error")
    code = request.query_params.get("code")
    state = request.query_params.get("state")
    stored_state = request.cookies.get("auth_state")

    # Debugging prints
    print(f"Received state: {state}")
    print(f"Stored state: {stored_state}")

    if error:
        return RedirectResponse(FRONTEND_HOME_URL)
    
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not found")
    
    if state != stored_state:
        raise HTTPException(status_code=403, detail="Invalid state parameter")
    
    # User accepts request. Exchange code for token
    token_json, token_error = exchange_code_for_token(code)
    if token_error:
        raise HTTPException(status_code=400, detail=f"Failed to retrieve access token: {token_error}")
    
    # Retrieve user info from Spotify
    user_json, user_error = get_spotify_user_info(token_json["access_token"])
    if user_error:
        raise HTTPException(status_code=400, detail=f"Failed to retrieve user info: {user_error}")

    save_or_update_user(db, user_json, token_json)

    return RedirectResponse(FRONTEND_APP_URL)