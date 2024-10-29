from fastapi import FastAPI, Depends, status, HTTPException
from database import engine
from typing import Annotated
from dependencies import db_dependency 
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: None, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return {
        "User": user
    }