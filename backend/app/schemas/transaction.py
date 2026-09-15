from pydantic import BaseModel
from datetime import date
from typing import Literal

class TransactionResponse(BaseModel):
    type: Literal["DEPOSIT", "WITHDRAW"]
    amount: float
    transaction_date: date