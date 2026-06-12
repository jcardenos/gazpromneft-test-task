from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

from auth import create_access_token, decode_token


app = FastAPI(title="JWT auth", version="1")
security = HTTPBearer()


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


users_db: dict[str, dict[str, str]] = {}


def get_current_username(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> str:
    payload = decode_token(credentials.credentials)
    username = payload["sub"]

    if username not in users_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный токен")

    return username


@app.post("/register", status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest) -> dict[str, str]:
    if payload.username in users_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Пользователь с таким именем уже существует")

    users_db[payload.username] = {
        "email": payload.email,
        "password": payload.password,
    }
    return {"message": "User created"}


@app.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest) -> TokenResponse:
    user = users_db.get(payload.username)

    if user is None or user["password"] != payload.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неправильное имя пользователя или пароль")

    return TokenResponse(access_token=create_access_token(payload.username))


@app.get("/protected")
def protected_route(username: str = Depends(get_current_username)) -> dict[str, str]:
    return {"message": "Это защищенный путь", "username": username}
