from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from app.services.jwt_service import decode_token
from app.schemas import UserRead

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def _unauthorized():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserRead:
    payload = decode_token(token)
    if payload is None:
        raise _unauthorized()
    user_id = payload.get("sub")
    email = payload.get("email")
    if not user_id or not email:
        raise _unauthorized()
    return UserRead(id=user_id, email=email)
