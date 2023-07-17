def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }


# Entity its an alternative name for a plural users in this case, could be named whatever
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
