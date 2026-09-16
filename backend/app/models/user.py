from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
