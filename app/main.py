# from fastapi import FastAPI, Depends, status, HTTPException
from fastapi import FastAPI
from app.database import engine
# from typing import Annotated
from app.router.api import user
from app.router import token
# from app.dependencies import db_dependency
import app.models.users as models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# ROUTER
app.include_router(user.router)
app.include_router(token.router)


# @app.get("/", status_code=status.HTTP_200_OK)
# async def user(user: None, db: db_dependency):
#     if user is None:
#         raise HTTPException(status_code=401, detail="Authentication failed")
#     return {
#         "User": user
#     }