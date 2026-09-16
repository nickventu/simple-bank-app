from sqlalchemy import Column, Integer, String, TIMESTAMP, Numeric, ForeignKey, func
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    txn_id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey("accounts.account_id"))
    txn_type = Column(String(20))
    amount = Column(Numeric(10,2))
    created_at = Column(TIMESTAMP, server_default=func.now())
