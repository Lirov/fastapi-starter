from fastapi import HTTPException, status
from app.schemas import UserCreate, LoginRequest, Token, UserRead
from app.services.user_service import user_service
from app.services.jwt_service import create_access_token

def register_user(user_in: UserCreate) -> UserRead:
    try:
        return user_service.create_user(user_in)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User already exists"
        )

def login_user(credentials: LoginRequest) -> Token:
    rec = user_service.get_by_email(credentials.email)
    if not rec or not user_service.verify_password(credentials.password, rec.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(subject=rec.id, email=rec.email)
    return Token(access_token=token)
