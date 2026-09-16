from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import user_service
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user(payload:UserCreate, db : Session = Depends(get_db)):
    user = user_service.create_user(db, payload.name, payload.email)
    return UserResponse(userId=user.user_id, name = user.name, email = user.email)
