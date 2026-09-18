from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.auth_service import authenticate_user, create_access_token
from app.schemas.auth import LoginRequest, TokenResponse

router = APIRouter()

@router.post("/auth/login", response_model = TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail = "Invalid email or password")
    token = create_access_token({"sub": str(user.user_id)})
    return TokenResponse(access_token = token, token_type = "bearer")