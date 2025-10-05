from typing import Optional, Dict
from passlib.context import CryptContext
from uuid import uuid4
from app.schemas import UserCreate, UserRead

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRecord:
    def __init__(self, email: str, password_hash: str):
        self.id = str(uuid4())
        self.email = email
        self.password_hash = password_hash

class UserService:
    """
    Simple in-memory user store. Swap this class for a DB-backed implementation later
    without changing controllers/routes.
    """
    def __init__(self):
        self._users_by_email: Dict[str, UserRecord] = {}

    def get_by_email(self, email: str) -> Optional[UserRecord]:
        return self._users_by_email.get(email.lower())

    def verify_password(self, plain_password: str, password_hash: str) -> bool:
        return pwd_context.verify(plain_password, password_hash)

    def hash_password(self, plain_password: str) -> str:
        return pwd_context.hash(plain_password)

    def create_user(self, user_in: UserCreate) -> UserRead:
        if self.get_by_email(user_in.email):
            raise ValueError("User already exists")
        record = UserRecord(
            email=user_in.email.lower(),
            password_hash=self.hash_password(user_in.password),
        )
        self._users_by_email[record.email] = record
        return UserRead(id=record.id, email=record.email)

# Singleton for simplicity
user_service = UserService()
