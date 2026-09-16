from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, name: str, email: str):
    new_user = User(name = name, email = email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: int):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        raise ValueError("User does not exist")
    return user
