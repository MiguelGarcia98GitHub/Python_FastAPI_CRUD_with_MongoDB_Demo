from fastapi import APIRouter, Response
from config.db import database
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

user = APIRouter()


@user.get("/users", response_model=List[User], tags=["users"])
async def find_all_user():
    return usersEntity(database.user.find())


@user.post("/users", response_model=User, tags=["users"])
async def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    id = database.user.insert_one(new_user).inserted_id

    user = database.user.find_one({"_id": id})

    return userEntity(user)


@user.get("/users/{id}", response_model=User, tags=["users"])
async def find_user(id: str):
    return userEntity(database.user.find_one({"_id": ObjectId(id)}))


@user.put("/users/{id}", response_model=User, tags=["users"])
async def update_user(id: str, user: User):
    updated_user = database.user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)}, return_document=True
    )
    return userEntity(updated_user)


@user.delete("/users/{id}", tags=["users"])
async def delete_user(id: str):
    userEntity(database.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
