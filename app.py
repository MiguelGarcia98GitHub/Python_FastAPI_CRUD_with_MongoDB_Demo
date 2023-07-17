from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API: FastAPI + MongoDB",
    description="simple users REST API for learning purposes using FastAPI + MongoDB",
    version="0.0.1"
)

app.include_router(user)
