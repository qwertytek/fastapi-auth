# from fastapi import APIRouter, HTTPException, Depends
from fastapi import APIRouter
# from fastapi.security import OAuth2PasswordBearer
from app.models.users import Users

router = APIRouter(
    prefix="/api/user",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{user_id}")
async def read_items(user_id: str):
    return user_id