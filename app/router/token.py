import os
from dotenv import load_dotenv
from fastapi import APIRouter
# from fastapi.security import OAuth2PasswordBearer
from app.models.users import Users

load_dotenv()

router = APIRouter(
    prefix="/token",
    tags=["token"],
    responses={404: {"description": "Not found"}},
)

secret_key = os.getenv('AUTH_SECRET_KEY', 'not set')

@router.get("/")
async def get_token():
    return {
        "token":f'{secret_key}'
    }