from fastapi import APIRouter
from typing import Union
from models.simpleModels import User, UserBD

users_router = APIRouter()


def coder_password(password: str):
    return ''.join(map(str, [ord(i) for i in password]))


def find_user(id: int):
    for user in users_list:
        if user.id == id:
            return user

    return None


users_list = [UserBD(name="Ivan", id=13, password=coder_password("password")),
              UserBD(name="Dima", id=16, password=coder_password("12345678"))]


@users_router.get("/api/users", response_model=Union[list[User], None])
def get_user():
    return users_list


@users_router.get("/api/users/{id}", response_model=Union[User, None])
def get_user_id(id: int):
    return find_user(id)


@users_router.post("/api/users")
def create_user(item: UserBD):
    if find_user(item.id) is not None:
        return {"message": "User with this id has already been created!"}

    user = UserBD(name=item.name, id=item.id, password=coder_password(item.password))
    users_list.append(user)

    return {"message": "User created successfully!"}


@users_router.put("/api/users/")
def edit_user(item: User):
    user = find_user(item.id)
    if user is None:
        return {"message": "User with this id does not exist!"}

    user.name = item.name
    return {"message": "Changed successfully!"}


@users_router.delete("/api/users/{id}")
def delete_user(id: int):
    user = find_user(id)
    if user is None:
        return {"message": "User with this id does not exist!"}

    users_list.remove(user)
    return {"message": "Delete successfully!"}
