from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI(title="CRUD", version="1")


class UserCreate(BaseModel):
    name: str
    email: str


class User(UserCreate):
    id: int


users: list[User] = []
next_id = 1


def get_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@app.get("/users", response_model=list[User])
def list_users() -> list[User]:
    return users


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int) -> User:
    return get_user(user_id)


@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate) -> User:
    global next_id

    new_user = User(id=next_id, name=user.name, email=user.email)
    users.append(new_user)
    next_id += 1
    return new_user


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate) -> User:
    current_user = get_user(user_id)
    current_user.name = user.name
    current_user.email = user.email
    return current_user


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int) -> None:
    user = get_user(user_id)
    users.remove(user)
