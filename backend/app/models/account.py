from sqlalchemy import Column, Integer, String, TIMESTAMP, Numeric, ForeignKey, func
from app.database import Base

class Account(Base):
    __tablename__ = "accounts"

    account_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    balance = Column(Numeric(10, 2), default= 0)
    account_type = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())
