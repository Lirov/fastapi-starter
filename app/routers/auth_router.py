from fastapi import APIRouter, Depends
from app.schemas import UserCreate, LoginRequest, Token, UserRead
from app.controllers.auth_controller import register_user, login_user
from app.core.security import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead)
def register(user_in: UserCreate):
    return register_user(user_in)

@router.post("/login", response_model=Token)
def login(credentials: LoginRequest):
    return login_user(credentials)

@router.get("/me", response_model=UserRead)
def me(current_user: UserRead = Depends(get_current_user)):
    return current_user
